#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <time.h>
#include <string.h>

#define FILE_NAME "testfile.bin"
#define FILE_SIZE (100 * 1024 * 1024) // 100MB
#define READ_SIZE (4 * 1024)  // 4KB
#define WRITE_SIZE (2 * 1024) // 2KB
#define NUM_OPERATIONS 50000  // 50,000 次隨機讀取或寫入

// 計算時間差
double get_time_diff(struct timespec start, struct timespec end) {
    return (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1e9;
}

// 建立 100MB 檔案
void create_test_file() {
    int fd = open(FILE_NAME, O_CREAT | O_WRONLY | O_TRUNC, 0644);
    if (fd == -1) {
        perror("open");
        exit(1);
    }

    char buffer[WRITE_SIZE];
    memset(buffer, 'A', WRITE_SIZE); // 填滿 'A'

    for (size_t i = 0; i < FILE_SIZE / WRITE_SIZE; i++) {
        if (write(fd, buffer, WRITE_SIZE) != WRITE_SIZE) {
            perror("write");
            close(fd);
            exit(1);
        }
    }
    close(fd);
    printf("100MB 檔案已建立。\n");
}

// 測量順序讀取時間
void measure_sequential_read() {
    int fd = open(FILE_NAME, O_RDONLY);
    if (fd == -1) {
        perror("open");
        exit(1);
    }

    char buffer[READ_SIZE];
    struct timespec start, end;

    clock_gettime(CLOCK_MONOTONIC, &start);
    while (read(fd, buffer, READ_SIZE) > 0);
    clock_gettime(CLOCK_MONOTONIC, &end);

    printf("順序讀取時間： %.6f seconds\n", get_time_diff(start, end));
    close(fd);
}

// 測量順序寫入時間
void measure_sequential_write() {
    int fd = open(FILE_NAME, O_WRONLY);
    if (fd == -1) {
        perror("open");
        exit(1);
    }

    char buffer[WRITE_SIZE];
    memset(buffer, 'B', WRITE_SIZE); // 填滿 'B'
    struct timespec start, end;

    clock_gettime(CLOCK_MONOTONIC, &start);
    for (size_t i = 0; i < FILE_SIZE / WRITE_SIZE; i++) {
        if (write(fd, buffer, WRITE_SIZE) != WRITE_SIZE) {
            perror("write");
            close(fd);
            exit(1);
        }
        fsync(fd); // 強制將資料寫入磁碟
    }
    clock_gettime(CLOCK_MONOTONIC, &end);

    printf("順序寫入時間： %.6f seconds\n", get_time_diff(start, end));
    close(fd);
}

// 測量隨機讀取時間
void measure_random_read() {
    int fd = open(FILE_NAME, O_RDONLY);
    if (fd == -1) {
        perror("open");
        exit(1);
    }

    char buffer[READ_SIZE];
    struct timespec start, end;
    srand(time(NULL)); // 設定隨機種子

    clock_gettime(CLOCK_MONOTONIC, &start);
    for (size_t i = 0; i < NUM_OPERATIONS; i++) {
        off_t offset = (rand() % (FILE_SIZE / READ_SIZE)) * READ_SIZE; // 4KB 對齊
        if (lseek(fd, offset, SEEK_SET) == -1) {
            perror("lseek");
            close(fd);
            exit(1);
        }
        if (read(fd, buffer, READ_SIZE) != READ_SIZE) {
            perror("read");
            close(fd);
            exit(1);
        }
    }
    clock_gettime(CLOCK_MONOTONIC, &end);

    printf("隨機讀取時間: %.6f seconds\n", get_time_diff(start, end));
    close(fd);
}

// 測量隨機緩衝寫入時間（無同步）
void measure_random_buffered_write_1() {
    int fd = open(FILE_NAME, O_RDWR);
    if (fd == -1) {
        perror("open");
        exit(1);
    }

    char buffer[WRITE_SIZE];
    memset(buffer, 'C', WRITE_SIZE);
    struct timespec start, end;
    srand(time(NULL));

    clock_gettime(CLOCK_MONOTONIC, &start);
    for (size_t i = 0; i < NUM_OPERATIONS; i++) {
        off_t offset = (rand() % (FILE_SIZE / READ_SIZE)) * READ_SIZE; // 4KB 對齊
        if (lseek(fd, offset, SEEK_SET) == -1) {
            perror("lseek");
            close(fd);
            exit(1);
        }
        if (write(fd, buffer, WRITE_SIZE) != WRITE_SIZE) {
            perror("write");
            close(fd);
            exit(1);
        }
    }
    fsync(fd); // 最後一次同步
    clock_gettime(CLOCK_MONOTONIC, &end);

    printf("隨機緩衝寫入（無同步）時間: %.6f seconds\n", get_time_diff(start, end));
    close(fd);
}

// 測量隨機緩衝寫入時間（每次寫入後立即 fsync）
void measure_random_buffered_write_2() {
    int fd = open(FILE_NAME, O_RDWR);
    if (fd == -1) {
        perror("open");
        exit(1);
    }

    char buffer[WRITE_SIZE];
    memset(buffer, 'D', WRITE_SIZE);
    struct timespec start, end;
    srand(time(NULL));

    clock_gettime(CLOCK_MONOTONIC, &start);
    for (size_t i = 0; i < NUM_OPERATIONS; i++) {
        off_t offset = (rand() % (FILE_SIZE / READ_SIZE)) * READ_SIZE; // 4KB 對齊
        if (lseek(fd, offset, SEEK_SET) == -1) {
            perror("lseek");
            close(fd);
            exit(1);
        }
        if (write(fd, buffer, WRITE_SIZE) != WRITE_SIZE) {
            perror("write");
            close(fd);
            exit(1);
        }
        fsync(fd); // 每次寫入後立即同步
    }
    clock_gettime(CLOCK_MONOTONIC, &end);

    printf("隨機緩衝寫入（每次同步）時間: %.6f seconds\n", get_time_diff(start, end));
    close(fd);
}

int main() {
    create_test_file();               // 建立 100MB 測試檔案
    measure_sequential_read();        // 測量順序讀取
    measure_sequential_write();       // 測量順序寫入
    measure_random_read();            // 測量隨機讀取
    measure_random_buffered_write_1();// 測量隨機緩衝寫入（無同步）
    measure_random_buffered_write_2();// 測量隨機緩衝寫入（每次寫入後立即同步）
    return 0;
}
