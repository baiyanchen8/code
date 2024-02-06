#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

volatile int lock = 0;  // 初始狀態鎖是空閒的

void critical_section(int i) {
    // 這裡放置臨界區的程式碼
    printf("%d\n", i);
}

void* thread_function(void* arg) {
    int i = *((int*)arg);  // 將 arg 轉換為整數
    while (lock != 0);  // 自旋直到鎖是空閒的
    lock = 1;  // 取得鎖
    critical_section(i);  // 進入臨界區
    lock = 0;  // 釋放鎖

    pthread_exit(NULL);
}

int main() {
    const int num_threads = 2;
    pthread_t threads[num_threads];
    int i;

    // 創建兩個執行緒
    for (i = 0; i < num_threads; ++i) {
        if (pthread_create(&threads[i], NULL, thread_function, &i) != 0) {
            fprintf(stderr, "執行緒創建失敗\n");
            exit(EXIT_FAILURE);
        }
    }

    // 等待執行緒結束
    for (i = 0; i < num_threads; ++i) {
        pthread_join(threads[i], NULL);
    }

    return 0;
}

