#include <stdio.h>
#include <stdlib.h>

// 定義佇列結構
struct queue {
    int *arr;   // 儲存元素的陣列
    int head;   // 佇列頭
    int tail;   // 佇列尾
    int count;  // 佇列容量
};

// 初始化佇列，並指定初始容量
void Q_init(struct queue *Q, int capacity) {
    Q->arr = (int *)malloc(capacity * sizeof(int));  // 分配記憶體給陣列
    Q->head = 0;
    Q->tail = 0;
    Q->count = capacity;
}

// 重新配置佇列容量
void Q_resize(struct queue *Q, int new_capacity) {
    Q->arr = (int *)realloc(Q->arr, new_capacity * sizeof(int));  // 重新配置記憶體
    Q->count = new_capacity;
}

// 入佇列
void enQ(struct queue *Q, int num) {
    if ((Q->tail + 1) % Q->count == Q->head) {
        // 佇列已滿，需要擴充容量
        int new_capacity = Q->count * 2;
        Q_resize(Q, new_capacity);
    }

    Q->tail = (Q->tail + 1) % Q->count;
    Q->arr[Q->tail - 1] = num;
}

// 出佇列
int deQ(struct queue *Q) {
    if (Q->head == Q->tail) {
        // 佇列為空，返回特殊值（這裡假設佇列存儲的元素為正整數）
        return -1;
    }

    int re = Q->arr[Q->head];
    Q->head = (Q->head + 1) % Q->count;

    // 檢查是否可以縮減容量
    if (Q->count > 20 && (Q->tail + 1) % Q->count <= Q->head) {
        int new_capacity = Q->count / 2;
        Q_resize(Q, new_capacity);
    }

    return re;
}

// 釋放佇列的記憶體
void Q_free(struct queue *Q) {
    free(Q->arr);
}

// 測試程式碼
int main() {
    struct queue myQueue;
    Q_init(&myQueue, 20);  // 初始容量為 20
	int i;
    // 將數字 1 到 25 放入佇列
    for (i = 1; i <= 240; i++) {
        enQ(&myQueue, i);
    }

    // 出佇列並印出
    for ( i = 0; i < 240; i++) {
        printf("%d ", deQ(&myQueue));
    }

    // 釋放佇列的記憶體
    Q_free(&myQueue);

    return 0;
}

