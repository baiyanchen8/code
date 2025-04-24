#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <time.h>
#include <sys/time.h>
#include <string.h>

#define FILE_NAME "testfile.bin"
#define FILE_SIZE (100 * 1024 * 1024) // 100MB
#define READ_SIZE 4096   // 4KB
#define WRITE_SIZE 2048  // 2KB
#define NUM_OPERATIONS 50000 // 執行 50,000 次隨機讀取或寫入

// 計時函式
double get_time() {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec + ts.tv_nsec * 1e-9;
}

// 建立 100MB 檔案
void create_file() {
    FILE *file = fopen(FILE_NAME, "wb");
    if (!file) {
        perror("fopen");
        exit(1);
    }

    char buffer[WRITE_SIZE];
    memset(buffer, 'A', WRITE_SIZE); // 用 'A' 填充緩衝區
    for (size_t i = 0; i < FILE_SIZE / WRITE_SIZE; i++) {
        fwrite(buffer, 1, WRITE_SIZE, file);
    }
    fclose(file);
    printf("100MB 檔案已建立。\n");
}

// 順序讀取測試（每次讀取 4KB）
void sequential_read() {
    FILE *file = fopen(FILE_NAME, "rb");
    if (!file) {
        perror("fopen");
        return;
    }

    char buffer[READ_SIZE];
    size_t bytesRead;
    double start = get_time();

    while ((bytesRead = fread(buffer, 1, READ_SIZE, file)) > 0) {
        // 讀取但不處理數據
    }

    double end = get_time();
    fclose(file);
    printf("順序讀取時間：%.6f 秒\n", end - start);
}

// 順序寫入測試（每次寫入 2KB 並 fsync）
void sequential_write() {
    int fd = open(FILE_NAME, O_WRONLY | O_CREAT | O_TRUNC, 0666);
    if (fd < 0) {
        perror("open");
        return;
    }

    char buffer[WRITE_SIZE];
    memset(buffer, 'B', WRITE_SIZE); // 用 'B' 填充緩衝區
    double start = get_time();

    for (size_t i = 0; i < FILE_SIZE / WRITE_SIZE; i++) {
        if (write(fd, buffer, WRITE_SIZE) < 0) {
            perror("write");
            close(fd);
            return;
        }
        fsync(fd); // 確保資料寫入磁碟
    }

    double end = get_time();
    close(fd);
    printf("順序寫入時間：%.6f 秒\n", end - start);
}

// 隨機讀取測試（50,000 次，每次讀取 4KB）
void random_read() {
    int fd = open(FILE_NAME, O_RDONLY);
    if (fd < 0) {
        perror("open");
        return;
    }

    char buffer[READ_SIZE];
    double start = get_time();

    for (size_t i = 0; i < NUM_OPERATIONS; i++) {
        off_t offset = (rand() % (FILE_SIZE / READ_SIZE)) * READ_SIZE; // 4KB 對齊
        if (lseek(fd, offset, SEEK_SET) == -1) {
            perror("lseek");
            close(fd);
            return;
        }
        if (read(fd, buffer, READ_SIZE) < 0) {
            perror("read");
            close(fd);
            return;
        }
    }

    double end = get_time();
    close(fd);
    printf("隨機讀取時間：%.6f 秒\n", end - start);
}

// 隨機緩衝寫入測試 1（50,000 次，每次寫入 2KB，不立即 fsync）
void random_buffered_write_1() {
    FILE *file = fopen(FILE_NAME, "r+b");
    if (!file) {
        perror("fopen");
        return;
    }

    char buffer[WRITE_SIZE];
    memset(buffer, 'C', WRITE_SIZE);
    double start = get_time();

    for (size_t i = 0; i < NUM_OPERATIONS; i++) {
        long offset = (rand() % (FILE_SIZE / READ_SIZE)) * READ_SIZE; // 4KB 對齊
        if (fseek(file, offset, SEEK_SET) != 0) {
            perror("fseek");
            fclose(file);
            return;
        }
        if (fwrite(buffer, 1, WRITE_SIZE, file) != WRITE_SIZE) {
            perror("fwrite");
            fclose(file);
            return;
        }
    }

    fflush(file); // 寫完再 flush
    int fd = fileno(file);
    fsync(fd);    // 實體同步到磁碟
    double end = get_time();
    fclose(file);
    printf("隨機緩衝寫入（不立即同步)：%.6f 秒\n", end - start);
}


// 隨機緩衝寫入測試 2（50,000 次，每次寫入 2KB，寫入後立即 fsync）
void random_buffered_write_2() {
    FILE *file = fopen(FILE_NAME, "r+b");
    if (!file) {
        perror("fopen");
        return;
    }

    char buffer[WRITE_SIZE];
    memset(buffer, 'D', WRITE_SIZE);
    double start = get_time();

    for (size_t i = 0; i < NUM_OPERATIONS; i++) {
        long offset = (rand() % (FILE_SIZE / READ_SIZE)) * READ_SIZE;
        if (fseek(file, offset, SEEK_SET) != 0) {
            perror("fseek");
            fclose(file);
            return;
        }
        if (fwrite(buffer, 1, WRITE_SIZE, file) != WRITE_SIZE) {
            perror("fwrite");
            fclose(file);
            return;
        }

        fflush(file);         // flush stdio buffer
        fsync(fileno(file));  // 實體同步
    }

    double end = get_time();
    fclose(file);
    printf("隨機緩衝寫入（每次同步）：%.6f 秒\n", end - start);
}


int main() {
    srand(time(NULL)); // 設定隨機種子

    create_file();             // 建立 100MB 測試檔案
    sequential_read();         // 測試順序讀取
    sequential_write();        // 測試順序寫入
    random_read();             // 測試隨機讀取
    random_buffered_write_1(); // 測試隨機緩衝寫入（不立即 fsync）
    random_buffered_write_2(); // 測試隨機緩衝寫入（每次寫入後立即 fsync）

    return 0;
}
