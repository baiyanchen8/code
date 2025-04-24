#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <time.h>
#include <aio.h>
#include <errno.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/wait.h>

#define BUF_SIZE 4096
#define MATRIX_SIZE 512
#define MAX_CONCURRENT 32

// 時間測量
void print_elapsed(struct timespec start, struct timespec end, const char* label) {
    double elapsed = (end.tv_sec - start.tv_sec) +
                     (end.tv_nsec - start.tv_nsec) / 1e9;
    printf("[%s] 執行時間：%.6f 秒\n", label, elapsed);
}

// 建立 input.txt 測試檔案
void generate_input_file() {
    if (access("input.txt", F_OK) == -1) {
        char choice;
        printf("⚙️ 找不到測試檔案 input.txt，是否建立 10MB 測試檔？(y/n)：");
        scanf(" %c", &choice);
        if (choice == 'y' || choice == 'Y') {
            printf("📦 正在產生 input.txt...\n");
            printf("use cmd :\'\033[1;33m dd if=/dev/urandom of=input.txt bs=1M count=10 status=none \033[0m\'\n");
            system("dd if=/dev/urandom of=input.txt bs=1M count=10 status=none");
            printf("✅ 檔案產生完成。\n");
        } else {
            printf("❌ 未建立檔案，請手動準備 input.txt。\n");
            exit(1);
        }
    }
}

// 清除 page cache
void clear_cache() {
    printf("📦 清除 Page Cache...\n");
    printf("use cmd :\'\033[1;33msync; echo 3 | sudo tee /proc/sys/vm/drop_caches > /dev/null\033[0m\'\n");
    system("sync; echo 3 | sudo tee /proc/sys/vm/drop_caches > /dev/null");
}

// ---------- Blocking I/O ----------
void blocking_io_copy(const char* input, const char* output) {
    int in_fd = open(input, O_RDONLY);
    int out_fd = open(output, O_WRONLY | O_CREAT | O_TRUNC, 0644);

    char buffer[BUF_SIZE];
    ssize_t bytes;
    while ((bytes = read(in_fd, buffer, BUF_SIZE)) > 0) {
        write(out_fd, buffer, bytes);
    }

    close(in_fd);
    close(out_fd);
}
// ---------- Matrix Multiplication ----------
int** alloc_matrix(int N) {
    int **mat = malloc(N * sizeof(int*));
    for (int i = 0; i < N; i++) {
        mat[i] = malloc(N * sizeof(int));
    }
    return mat;
}

void fill_matrix(int** mat, int N) {
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            mat[i][j] = rand() % 10;
}

void multiply_matrix(int** A, int** B, int** C, int N) {
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++) {
            C[i][j] = 0;
            for (int k = 0; k < N; k++)
                C[i][j] += A[i][k] * B[k][j];
        }
}

void free_matrix(int** mat, int N) {
    for (int i = 0; i < N; i++)
        free(mat[i]);
    free(mat);
}
// ---------- Blocking I/O  +Matrix Multiplication----------
void blocking_io_copy_matrix_multiplication(const char* input, const char* output) {
    int in_fd = open(input, O_RDONLY);
    int out_fd = open(output, O_WRONLY | O_CREAT | O_TRUNC, 0644);
    off_t file_size = lseek(in_fd, 0, SEEK_END);
    lseek(in_fd, 0, SEEK_SET); // 回到開頭
    char* buffer = malloc(file_size);

    ssize_t total_read = 0;
    while (total_read < file_size) {
        ssize_t bytes = read(in_fd, buffer + total_read, file_size - total_read);
        if (bytes < 0) {
            perror("❌ 讀取檔案失敗");
            free(buffer);
            close(in_fd);
            close(out_fd);
            return;
        }
        total_read += bytes;
    }

    // ⚙️ 執行矩陣乘法運算
    printf("⚙️ 執行矩陣乘法運算...\n");
    int **A = alloc_matrix(MATRIX_SIZE);
    int **B = alloc_matrix(MATRIX_SIZE);
    int **C = alloc_matrix(MATRIX_SIZE);
    fill_matrix(A, MATRIX_SIZE);
    fill_matrix(B, MATRIX_SIZE);
    multiply_matrix(A, B, C, MATRIX_SIZE);
    free_matrix(A, MATRIX_SIZE);
    free_matrix(B, MATRIX_SIZE);
    free_matrix(C, MATRIX_SIZE);

    // ✍️ 寫出整個檔案
    ssize_t total_written = 0;
    while (total_written < file_size) {
        ssize_t bytes = write(out_fd, buffer + total_written, file_size - total_written);
        if (bytes < 0) {
            perror("❌ 寫入檔案失敗");
            break;
        }
        total_written += bytes;
    }

    free(buffer);
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
// ---------- AIO_concurrency + Matrix Multiplication ----------
void aio_with_matrix_concurrency(const char* input, const char* output,int concurrent) {
    int fd = open(input, O_RDONLY);
    int out_fd = open(output, O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (fd < 0 || out_fd < 0) {
        perror("open");
        return;
    }

    off_t file_size = get_file_size(input);
    if (file_size < 0) {
        close(fd);
        close(out_fd);
        return;
    }

    // 根據檔案大小動態分配 buffer 數量
    int total_buffers = (file_size + BUF_SIZE - 1) / BUF_SIZE;
    int buffers_per_task = (total_buffers + concurrent - 1) / concurrent; 
    int super_buf_size = buffers_per_task * BUF_SIZE;

    struct aiocb cbs[concurrent];  // 支援 4 並發
    char* buffers[concurrent];
    for (int i = 0; i < concurrent; ++i) {
        buffers[i] = malloc(super_buf_size);
        if (!buffers[i]) {
            perror("malloc");
            return;
        }
    }

    // 開始讀取檔案，並執行矩陣運算
    off_t offset = 0;
    int remaining_buffers = total_buffers;
    while (remaining_buffers > 0) {
        int actual_tasks = remaining_buffers < concurrent ? remaining_buffers : concurrent;
        for (int i = 0; i < actual_tasks; ++i) {
            int read_count = buffers_per_task;
            if (read_count > remaining_buffers) {
                read_count = remaining_buffers;
            }

            memset(&cbs[i], 0, sizeof(struct aiocb));
            cbs[i].aio_fildes = fd;
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

        // 矩陣運算
        printf("⚙️ 執行矩陣運算...\nconcurrency");
        int **A = alloc_matrix(MATRIX_SIZE), **B = alloc_matrix(MATRIX_SIZE), **C = alloc_matrix(MATRIX_SIZE);
        fill_matrix(A, MATRIX_SIZE);
        fill_matrix(B, MATRIX_SIZE);
        multiply_matrix(A, B, C, MATRIX_SIZE);
        free_matrix(A, MATRIX_SIZE);
        free_matrix(B, MATRIX_SIZE);
        free_matrix(C, MATRIX_SIZE);

        // 等待 AIO 完成
        for (int i = 0; i < actual_tasks; ++i) {
            while (aio_error(&cbs[i]) == EINPROGRESS);
            ssize_t ret = aio_return(&cbs[i]);
            if (ret > 0) {
                write(out_fd, buffers[i], ret);
            }
        }
    }

    // 清理
    for (int i = 0; i < concurrent; ++i) {
        free(buffers[i]);
    }

    close(fd);
    close(out_fd);
}
//--------- AIO + Matrix Multiplication ----------
void aio_with_matrix(const char* input, const char* output) {
    int fd = open(input, O_RDONLY);
    int out_fd = open(output, O_WRONLY | O_CREAT | O_TRUNC, 0644);
    char* buffer = malloc(BUF_SIZE);

    struct aiocb cb;
    memset(&cb, 0, sizeof(cb));
    cb.aio_fildes = fd;
    cb.aio_buf = buffer;
    cb.aio_nbytes = BUF_SIZE;
    cb.aio_offset = 0;

    aio_read(&cb);

    // 計算矩陣乘法
    printf("⚙️ 執行矩陣運算...\n");
    int **A = alloc_matrix(MATRIX_SIZE), **B = alloc_matrix(MATRIX_SIZE), **C = alloc_matrix(MATRIX_SIZE);
    fill_matrix(A, MATRIX_SIZE);
    fill_matrix(B, MATRIX_SIZE);
    multiply_matrix(A, B, C, MATRIX_SIZE);
    free_matrix(A, MATRIX_SIZE);
    free_matrix(B, MATRIX_SIZE);
    free_matrix(C, MATRIX_SIZE);

    // Polling 等待 AIO 完成
    while (aio_error(&cb) == EINPROGRESS) {}

    ssize_t ret = aio_return(&cb);
    if (ret > 0) {
        write(out_fd, buffer, ret);
    }

    close(fd);
    close(out_fd);
    free(buffer);
} 
// ---------- 主程式 ----------
int main() {
    generate_input_file();

    while (1) {
        int choice;
        printf("\n========== I/O 模式選單 ==========\n");
        printf(" 1: Blocking I/O\n");
        printf(" 2: Asynchronous I/O (AIO)\n");
        printf(" 3: Blocking I/O + Matrix 計算\n");
        printf(" 4: AIO (Polling+concurrency) + Matrix 計算\n");
        printf(" 5: AIO (Polling) + Matrix 計算\n");
        printf(" 0: 離開程式\n");
        printf("請選擇模式：");
        scanf("%d", &choice);

        if (choice == 0) {
            printf("結束測試。\n");
            break;
        }

        clear_cache();

        struct timespec start, end;

        switch (choice) {
            case 1:
                printf("🔧 測試模式：Blocking I/O\n");
                clock_gettime(CLOCK_MONOTONIC, &start);
                blocking_io_copy("input.txt", "output_blocking.txt");
                clock_gettime(CLOCK_MONOTONIC, &end);
                print_elapsed(start, end, "Blocking I/O");
                break;
            case 2: {
                int concurrency;
                printf("請輸入 AIO 並發數量（目前範例忽略並發，固定為單一區塊）：");
                scanf("%d", &concurrency);
                printf("🔧 測試模式：Asynchronous I/O（Polling）\n");
                clock_gettime(CLOCK_MONOTONIC, &start);
                aio_io_copy("input.txt", "output_aio.txt",concurrency);
                clock_gettime(CLOCK_MONOTONIC, &end);
                print_elapsed(start, end, "AIO（Polling）");
                break;
            }
            case 3:
                printf("🔧 測試模式：Blocking I/O + Matrix\n");
                clock_gettime(CLOCK_MONOTONIC, &start);
                blocking_io_copy_matrix_multiplication("input.txt", "output_blocking.txt");
                clock_gettime(CLOCK_MONOTONIC, &end);
                print_elapsed(start, end, "Blocking + Matrix");
                break;
            case 4:
                int concurrency;
                printf("請輸入 AIO 並發數量（目前範例忽略並發，固定為單一區塊）：");
                scanf("%d", &concurrency);
                printf("🔧 測試模式：AIO(concurrency) + Matrix 運算\n");
                clock_gettime(CLOCK_MONOTONIC, &start);
                aio_with_matrix_concurrency("input.txt", "output_aio_calc.txt",concurrency);
                clock_gettime(CLOCK_MONOTONIC, &end);
                print_elapsed(start, end, "AIO + Matrix");
                break;
            case 5:
                printf("🔧 測試模式：AIO + Matrix 運算\n");
                clock_gettime(CLOCK_MONOTONIC, &start);
                aio_with_matrix("input.txt", "output_aio_calc.txt");
                clock_gettime(CLOCK_MONOTONIC, &end);
                print_elapsed(start, end, "AIO + Matrix");
                break;
            case 0:
                return 0;
            default:
                printf("❗ 無效選項，請重新輸入。\n");
                break;
        }
    }

    return 0;
}
