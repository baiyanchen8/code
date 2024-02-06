#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

volatile int turn = 0;
volatile int in_critical_section[4] = {0};
volatile int next = 0;

volatile int compare_and_swap(int *ptr, int expected, int new_value) {
    int result;
    asm volatile("lock; cmpxchg %2, %1" : "=a"(result) : "m"(*ptr), "r"(new_value), "0"(expected) : "memory");
    return result;
}

void critical_section(int thread_id) {
    // 在這裡放置臨界區的程式碼
    printf("執行緒 %d 進入臨界區 next: %d\n", thread_id, next);
}

void* thread_function(void* arg) {
    int thread_id = *((int*)arg);
    int i = 0;

    while (i < 10) {
        // 檢查是否輪到自己進入臨界區，且臨界區是否空閒
        
		while (compare_and_swap(&turn, thread_id, next) != thread_id  ) {;}
        // 標記臨界區為自己的狀態
		while (in_critical_section[thread_id] == 1) {;}
		
        in_critical_section[thread_id] = 1;
    
        // 進入臨界區
        critical_section(thread_id);
//        sleep(1);

        // 離開臨界區，並將 next 設為下一個執行緒
        next = (turn + 1) % 4;
        if (turn == thread_id)
        	turn = (turn + 1) % 4;
        in_critical_section[turn] = 0;
        
        i++;
    }

    pthread_exit(NULL);
}

int main() {
    const int num_threads = 4;
    pthread_t threads[num_threads];
    int thread_ids[num_threads];
    int i;

    // 創建四個執行緒
    for (i = 0; i < num_threads; ++i) {
        thread_ids[i] = i;
        in_critical_section[i] = 1;
        if (pthread_create(&threads[i], NULL, thread_function, &thread_ids[i]) != 0) {
            fprintf(stderr, "執行緒創建失敗\n");
            exit(EXIT_FAILURE);
        }
    }
    next=1;
	in_critical_section[0] = 0;
    // 等待執行緒結束
    for (i = 0; i < num_threads; ++i) {
        pthread_join(threads[i], NULL);
    }

    return 0;
}

