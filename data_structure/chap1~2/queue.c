#include <stdio.h>
#include <stdlib.h>

struct Queue {
	int *init;
    int *arr;
    int len;
    int capacity;
};

// 初始化佇列
void Q_init(struct Queue *Q) {
	
    Q->arr = (int *)malloc(sizeof(int) * 20);
    Q->init=Q->arr; 
    Q->len = 0;
    Q->capacity = 20;
}

// 入佇列
void enqueue(struct Queue *Q, int num) {
    if (Q->len >= Q->capacity / 2) {
        Q->capacity *= 2;
        Q->arr = (int *)realloc(Q->arr, Q->capacity * sizeof(int));
    }
    Q->arr[Q->len++] = num;
}

// 出佇列
int deq(struct Queue *Q) {
    int ans = Q->arr[0];
    Q->len -= 1;
    Q->capacity -= 1;
	
    // 將陣列指標移動到下一個位置
    if (Q->len>0){
    	Q->arr += 1;
	}
    return ans;
}

int main() {
    struct Queue myQueue;
    Q_init(&myQueue); // 使用 '&' 來傳遞結構的指標

    int i;
    for (i = 0; i < 10; i++) {
        enqueue(&myQueue, i); // 使用 '&' 來傳遞結構的指標
    }

    printf("入佇列後的元素：");
    for (i = 0; i < myQueue.len; i++) {
        printf("%d  ", myQueue.arr[i]); // 修正印出陣列元素的方式
    }
    printf("\n");

    printf("出佇列的元素：");
    for (i = 0; i < 10; i++) {
        int t = deq(&myQueue);
        printf("%d  ", t); // 修正印出陣列元素的方式
    }
    printf("\n");
    // 釋放記憶體
    free(myQueue.init);

    return 0;
}

