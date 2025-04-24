#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/mman.h>
#include <sys/time.h>
#include <string.h>
#include <time.h>

#define FILE_NAME "testfile_mmap.dat"
#define FILE_SIZE (100 * 1024 * 1024)  // 100MB
#define READ_SIZE 4096   // 4KB
#define WRITE_SIZE 2048  // 2KB
#define NUM_OPERATIONS 50000  // 50,000 次隨機操作

// 取得當前時間（微秒）
double get_time_in_sec() {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return tv.tv_sec + tv.tv_usec / 1000000.0;
}

// 建立 100MB 測試檔案
void create_test_file() {
    int fd = open(FILE_NAME, O_CREAT | O_RDWR, 0666);
    if (fd < 0) {
        perror("Failed to create test file");
        exit(EXIT_FAILURE);
    }

    if (ftruncate(fd, FILE_SIZE) != 0) {
        perror("Failed to set file size");
        close(fd);
        exit(EXIT_FAILURE);
    }
    printf("100MB 檔案已建立。\n");
    close(fd);
}

// 測試 Memory-Mapped 順序讀取（4KB/次）
void mmap_sequential_read() {
    int fd = open(FILE_NAME, O_RDONLY);
    if (fd < 0) {
        perror("Failed to open file for reading");
        exit(EXIT_FAILURE);
    }

    char *mapped = mmap(NULL, FILE_SIZE, PROT_READ, MAP_PRIVATE, fd, 0);
    if (mapped == MAP_FAILED) {
        perror("mmap failed");
        close(fd);
        exit(EXIT_FAILURE);
    }

    char buffer[READ_SIZE];
    double start_time = get_time_in_sec();

    for (size_t i = 0; i < FILE_SIZE; i += READ_SIZE) {
        memcpy(buffer, mapped + i, READ_SIZE);  // 模擬讀取
    }

    double end_time = get_time_in_sec();
    printf("順序讀取(mamap)時間： %.6f seconds\n", end_time - start_time);

    munmap(mapped, FILE_SIZE);
    close(fd);
}

// 測試 Memory-Mapped 順序寫入（2KB/次，並呼叫 msync()）
void mmap_sequential_write() {
    int fd = open(FILE_NAME, O_RDWR);
    if (fd < 0) {
        perror("Failed to open file for writing");
        exit(EXIT_FAILURE);
    }

    char *mapped = mmap(NULL, FILE_SIZE, PROT_WRITE, MAP_SHARED, fd, 0);
    if (mapped == MAP_FAILED) {
        perror("mmap failed");
        close(fd);
        exit(EXIT_FAILURE);
    }

    char buffer[WRITE_SIZE];
    memset(buffer, 'B', WRITE_SIZE);
    double start_time = get_time_in_sec();

    for (size_t i = 0; i < FILE_SIZE; i += WRITE_SIZE) {
        memcpy(mapped + i, buffer, WRITE_SIZE);  // 寫入記憶體映射區域
        msync(mapped, FILE_SIZE, MS_SYNC);  // 確保資料寫入磁碟
    }

 
    double end_time = get_time_in_sec();
    printf("順序寫入(mmap)時間: %.6f seconds\n", end_time - start_time);

    munmap(mapped, FILE_SIZE);
    close(fd);
}

// 測試 Memory-Mapped 隨機讀取
void mmap_random_read() {
    int fd = open(FILE_NAME, O_RDONLY);
    if (fd < 0) {
        perror("Failed to open file for reading");
        exit(EXIT_FAILURE);
    }

    char *mapped = mmap(NULL, FILE_SIZE, PROT_READ, MAP_PRIVATE, fd, 0);
    if (mapped == MAP_FAILED) {
        perror("mmap failed");
        close(fd);
        exit(EXIT_FAILURE);
    }

    char buffer[READ_SIZE];
    double start_time = get_time_in_sec();
    srand(time(NULL));

    for (size_t i = 0; i < NUM_OPERATIONS; i++) {
        off_t offset = (rand() % (FILE_SIZE / READ_SIZE)) * READ_SIZE;
        memcpy(buffer, mapped + offset, READ_SIZE);  // 隨機讀取
    }

    double end_time = get_time_in_sec();
    printf("隨機讀取(mmap)時間： %.6f seconds\n", end_time - start_time);

    munmap(mapped, FILE_SIZE);
    close(fd);
}

// 測試 Memory-Mapped 隨機緩衝寫入（無同步）
void mmap_random_buffered_write_1() {
    int fd = open(FILE_NAME, O_RDWR);
    if (fd < 0) {
        perror("Failed to open file for writing");
        exit(EXIT_FAILURE);
    }

    char *mapped = mmap(NULL, FILE_SIZE, PROT_WRITE, MAP_SHARED, fd, 0);
    if (mapped == MAP_FAILED) {
        perror("mmap failed");
        close(fd);
        exit(EXIT_FAILURE);
    }

    char buffer[WRITE_SIZE];
    memset(buffer, 'C', WRITE_SIZE);
    double start_time = get_time_in_sec();
    srand(time(NULL));

    for (size_t i = 0; i < NUM_OPERATIONS; i++) {
        off_t offset = (rand() % (FILE_SIZE / READ_SIZE)) * READ_SIZE;
        memcpy(mapped + offset, buffer, WRITE_SIZE);  // 隨機寫入
    }

    msync(mapped, FILE_SIZE, MS_SYNC);  // 最後一次同步
    double end_time = get_time_in_sec();
    printf("隨機緩衝寫入（不立即同步)：%.6f seconds\n", end_time - start_time);

    munmap(mapped, FILE_SIZE);
    close(fd);
}

// 測試 Memory-Mapped 隨機緩衝寫入（每次寫入後立即同步）
void mmap_random_buffered_write_2() {
    int fd = open(FILE_NAME, O_RDWR);
    if (fd < 0) {
        perror("Failed to open file for writing");
        exit(EXIT_FAILURE);
    }

    char *mapped = mmap(NULL, FILE_SIZE, PROT_WRITE, MAP_SHARED, fd, 0);
    if (mapped == MAP_FAILED) {
        perror("mmap failed");
        close(fd);
        exit(EXIT_FAILURE);
    }

    char buffer[WRITE_SIZE];
    memset(buffer, 'D', WRITE_SIZE);
    double start_time = get_time_in_sec();
    srand(time(NULL));

    for (size_t i = 0; i < NUM_OPERATIONS; i++) {
        off_t offset = (rand() % (FILE_SIZE / READ_SIZE)) * READ_SIZE;
        memcpy(mapped + offset, buffer, WRITE_SIZE);  // 隨機寫入
        msync(mapped + offset, WRITE_SIZE, MS_SYNC);  // 每次寫入後立即同步
    }

    double end_time = get_time_in_sec();
    printf("隨機緩衝寫入（每次同步）：%.6f seconds\n", end_time - start_time);

    munmap(mapped, FILE_SIZE);
    close(fd);
}

int main() {
    create_test_file();
    mmap_sequential_read();
    mmap_sequential_write();
    mmap_random_read();
    mmap_random_buffered_write_1();
    mmap_random_buffered_write_2();
    return 0;
}
