#include <stdio.h>
#include <stdlib.h>

struct Queue {
	int *init;
    int *arr;
    int len;
    int capacity;
};

// ��l�Ʀ�C
void Q_init(struct Queue *Q) {
	
    Q->arr = (int *)malloc(sizeof(int) * 20);
    Q->init=Q->arr; 
    Q->len = 0;
    Q->capacity = 20;
}

void enqueue(struct Queue *Q, int num) {
    if (Q->len >= Q->capacity / 2) {
        Q->capacity *= 2;
        Q->arr = (int *)realloc(Q->arr, Q->capacity * sizeof(int));
    }
    Q->arr[Q->len++] = num;
}

int deq(struct Queue *Q) {
    int ans = Q->arr[0];
    Q->len -= 1;
    Q->capacity -= 1;
	
    if (Q->len>0){
    	Q->arr += 1;
	}
    return ans;
}

int main() {
    struct Queue myQueue;
    Q_init(&myQueue); // �ϥ� '&' �Ӷǻ����c������

    int i;
    for (i = 0; i < 10; i++) {
        enqueue(&myQueue, i); // �ϥ� '&' �Ӷǻ����c������
    }

    printf("�J��C�᪺�����G");
    for (i = 0; i < myQueue.len; i++) {
        printf("%d  ", myQueue.arr[i]); // �ץ��L�X�}�C�������覡
    }
    printf("\n");

    printf("�X��C�������G");
    for (i = 0; i < 10; i++) {
        int t = deq(&myQueue);
        printf("%d  ", t); // �ץ��L�X�}�C�������覡
    }
    printf("\n");
    // ����O����
    free(myQueue.init);

    return 0;
}

