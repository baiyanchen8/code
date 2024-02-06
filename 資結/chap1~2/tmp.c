#include <stdio.h>
#include <stdbool.h>
#include <pthread.h>
#include <unistd.h>

#define n 4

volatile bool waiting[n];
volatile bool lock = false;

// 使用 Test-and-Set 實現的鎖獲取函數
bool test_and_set(bool *target) {
    bool previous = *target;
    *target = true;
    return previous;
}

void* thread_function(void* arg) {
    int thread_id = *((int*)arg);
	int i=0;
    do {
        waiting[thread_id] = true;
		i++;
        while (waiting[thread_id] == true&& test_and_set(&lock)) {
            // 等待鎖釋放
        }

        waiting[thread_id] = false;

        // 進入臨界區
        printf("執行緒 %d 進入臨界區\n", thread_id);
        // 在這裡放置臨界區的程式碼
//        sleep(1);  // 模擬臨界區執行時間
        printf("執行緒 %d 離開臨界區\n", thread_id);

        int j = (thread_id + 1) % n;

        // 尋找下一個等待的執行緒
        while (j != thread_id && waiting[j]==false) {
            j = (j + 1) % n;
        }

        if (j == thread_id) {
            // 沒有等待的執行緒，釋放鎖
            lock = false;
        } else {
            // 通知下一個等待的執行緒進入臨界區
            waiting[j] = false;
        }

    } while (i<10);

    pthread_exit(NULL);
}

int main() {
    pthread_t threads[n];
    int thread_ids[n];
    int i;

    // 初始化等待狀態
    for (i = 0; i < n; ++i) {
        waiting[i] = false;
    }

    // 創建 n 個執行緒
    for (i = 0; i < n; ++i) {
        thread_ids[i] = i;
        if (pthread_create(&threads[i], NULL, thread_function, &thread_ids[i]) != 0) {
            fprintf(stderr, "執行緒創建失敗\n");
            return -1;
        }
    }
    // 主執行緒等待所有執行緒結束
    for (i = 0; i < n; ++i) {
        pthread_join(threads[i], NULL);
    }

    return 0;
}

