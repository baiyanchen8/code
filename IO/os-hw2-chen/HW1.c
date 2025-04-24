#define _GNU_SOURCE
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <aio.h>
#include <errno.h>
#include <time.h>
#include <stdlib.h> // for system()
#include <unistd.h> // for access()

#define BUF_SIZE 4096
#define MAX_CONCURRENT 32

void print_elapsed(struct timespec start, struct timespec end, const char* label) {
    double elapsed = (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1e9;
    printf("[%s] 執行時間：%.6f 秒\n", label, elapsed);
}

void blocking_io_copy(const char* src, const char* dst) {
    int in_fd = open(src, O_RDONLY);
    int out_fd = open(dst, O_WRONLY | O_CREAT | O_TRUNC, 0644);
    char buf[BUF_SIZE];
    ssize_t n;

    while ((n = read(in_fd, buf, sizeof(buf))) > 0) {
        write(out_fd, buf, n);
    }

    close(in_fd);
    close(out_fd);
}

void nonblocking_io_copy(const char* src, const char* dst) {
    int in_fd = open(src, O_RDONLY | O_NONBLOCK);
    int out_fd = open(dst, O_WRONLY | O_CREAT | O_TRUNC | O_NONBLOCK, 0644);
    char buf[BUF_SIZE];
    ssize_t n;

    while (1) {
        n = read(in_fd, buf, sizeof(buf));
        if (n > 0) {
            ssize_t written = 0;
            while (written < n) {        
                written += write(out_fd, buf + written, n - written);
            }
        } else if (n == 0) {
            break;
        } else if (errno != EAGAIN && errno != EWOULDBLOCK) {
            perror("read");
            break;
        }
    }

    close(in_fd);
    close(out_fd);
}

off_t get_file_size(const char* filename) {
    struct stat st;
    if (stat(filename, &st) != 0) {
        perror("stat");
        return -1;
    }
    return st.st_size;
}

void aio_io_copy(const char* src, const char* dst, int concurrent) {
    int in_fd = open(src, O_RDONLY);
    int out_fd = open(dst, O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (in_fd < 0 || out_fd < 0) {
        perror("open");
        return;
    }

    off_t file_size = get_file_size(src);
    if (file_size < 0) {
        close(in_fd);
        close(out_fd);
        return;
    }

    int total_buffers = (file_size + BUF_SIZE - 1) / BUF_SIZE;
    int buffers_per_task = (total_buffers + concurrent - 1) / concurrent;
    int super_buf_size = buffers_per_task * BUF_SIZE;

    struct aiocb cbs[MAX_CONCURRENT];
    char* buffers[MAX_CONCURRENT];
    off_t offset = 0;

    for (int i = 0; i < concurrent; ++i) {
        buffers[i] = malloc(super_buf_size);
        if (!buffers[i]) {
            perror("malloc");
            return;
        }
    }

    int remaining_buffers = total_buffers;
    while (remaining_buffers > 0) {
        int actual_tasks = remaining_buffers < concurrent ? remaining_buffers : concurrent;
        for (int i = 0; i < actual_tasks; ++i) {
            int read_count = buffers_per_task;
            if (read_count > remaining_buffers)
                read_count = remaining_buffers;

            memset(&cbs[i], 0, sizeof(struct aiocb));
            cbs[i].aio_fildes = in_fd;
            cbs[i].aio_buf = buffers[i];
            cbs[i].aio_nbytes = read_count * BUF_SIZE;
            cbs[i].aio_offset = offset;
            offset += cbs[i].aio_nbytes;

            if (aio_read(&cbs[i]) < 0) {
                perror("aio_read");
                return;
            }

            remaining_buffers -= read_count;
        }

        // 等待所有 AIO 完成
        for (int i = 0; i < actual_tasks; ++i) {
            while (aio_error(&cbs[i]) == EINPROGRESS);
            int bytes_read = aio_return(&cbs[i]);
            if (bytes_read <= 0) {
                fprintf(stderr, "aio_read failed or EOF\n");
                return;
            }

            struct aiocb write_cb;
            memset(&write_cb, 0, sizeof(struct aiocb));
            write_cb.aio_fildes = out_fd;
            write_cb.aio_buf = buffers[i];
            write_cb.aio_nbytes = bytes_read;
            write_cb.aio_offset = cbs[i].aio_offset;

            if (aio_write(&write_cb) < 0) {
                perror("aio_write");
                return;
            }

            while (aio_error(&write_cb) == EINPROGRESS);
            int bytes_written = aio_return(&write_cb);
            if (bytes_written != bytes_read) {
                fprintf(stderr, "aio_write incomplete\n");
                return;
            }
        }
    }

    for (int i = 0; i < concurrent; ++i) {
        free(buffers[i]);
    }

    close(in_fd);
    close(out_fd);
}

int main() {
    int mode;
    char filename[100] = "input.txt";
    struct timespec start, end;

    // 檢查是否有 input.txt，沒有就建立
    if (access(filename, F_OK) != 0) {
        printf("⚙️ 找不到測試檔案 input.txt，是否建立 10MB 測試檔？(y/n)：");
        char choice;
        scanf(" %c", &choice);
        if (choice == 'y' || choice == 'Y') {
            printf("📦 正在產生 input.txt...\n");
            printf("use cmd :\'\033[1;33m dd if=/dev/urandom of=input.txt bs=1M count=10 status=none \033[0m\'\n");

            int ret = system("dd if=/dev/urandom of=input.txt bs=1M count=10 status=none");
            if (ret != 0) {
                printf("❌ 無法建立測試檔案，請確認系統支援 dd 指令。\n");
                return 1;
            }
            printf("✅ 檔案產生完成。\n");
        } else {
            printf("⚠️ 未建立檔案，程式終止。\n");
            return 1;
        }
    }

    while (1) {
        printf("\n========== I/O 模式選單 ==========\n");
        printf(" 1: Blocking I/O\n");
        printf(" 2: Non-Blocking I/O\n");
        printf(" 3: Asynchronous I/O (AIO)\n");
        printf(" 0: 離開程式\n");
        printf("請選擇模式：");
        scanf("%d", &mode);

        if (mode == 0) {
            printf("結束測試。\n");
            break;
        }

        // 清除 Page Cache
        printf("\n📦 清除 Page Cache...\n");
        printf("use cmd :\'\033[1;33m sync; echo 3 | sudo tee /proc/sys/vm/drop_caches > /dev/null \033[0m\'\n");
        int clear_result = system("sync; echo 3 | sudo tee /proc/sys/vm/drop_caches > /dev/null");
        if (clear_result != 0) {
            printf("⚠️ 無法清除 Page Cache，請確認使用 sudo 執行。\n");
        }

        if (mode == 1) {
            printf("🔧 測試模式：Blocking I/O\n");
            clock_gettime(CLOCK_MONOTONIC, &start);
            blocking_io_copy(filename, "output_blocking.txt");
            clock_gettime(CLOCK_MONOTONIC, &end);
            print_elapsed(start, end, "Blocking I/O");

        } else if (mode == 2) {
            printf("🔧 測試模式：Non-Blocking I/O\n");
            clock_gettime(CLOCK_MONOTONIC, &start);
            nonblocking_io_copy(filename, "output_nonblocking.txt");
            clock_gettime(CLOCK_MONOTONIC, &end);
            print_elapsed(start, end, "Non-Blocking I/O");

        } else if (mode == 3) {
            int concurrent;
            printf("請輸入 AIO 並發數量（1~%d）：", MAX_CONCURRENT);
            scanf("%d", &concurrent);
            if (concurrent <= 0 || concurrent > MAX_CONCURRENT) concurrent = 4;

            printf("🔧 測試模式：Asynchronous I/O（%d 並發）\n", concurrent);
            clock_gettime(CLOCK_MONOTONIC, &start);
            aio_io_copy(filename, "output_aio.txt", concurrent);
            clock_gettime(CLOCK_MONOTONIC, &end);

            char label[64];
            sprintf(label, "AIO（並發數 %d）", concurrent);
            print_elapsed(start, end, label);
        } else {
            printf("⚠️ 無效的選項，請重新選擇。\n");
        }
    }

    return 0;
}
