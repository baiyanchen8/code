#include <stdio.h>
#include <stdlib.h>

#define MAX_HEAP_SIZE 100

// 定義 MaxHeap 結構
typedef struct {
    int heap[MAX_HEAP_SIZE];
    int size;
} MaxHeap;

// 初始化 MaxHeap
void init(MaxHeap *maxHeap) {
    maxHeap->size = 0;
}

// 獲取父節點的索引
int parent(int i) {
    return (i - 1) / 2;
}

// 獲取左子節點的索引
int leftChild(int i) {
    return 2 * i + 1;
}

// 獲取右子節點的索引
int rightChild(int i) {
    return 2 * i + 2;
}





// 上移操作（向上調整堆）
void heapifyUp(MaxHeap *maxHeap, int i) {
    int temp = maxHeap->heap[i];
    while (i > 0 && temp > maxHeap->heap[parent(i)]) {
        maxHeap->heap[i] = maxHeap->heap[parent(i)];
        i = parent(i);
    }
    maxHeap->heap[i] = temp;
}
// 插入操作
void insert(MaxHeap *maxHeap, int value) {
    if (maxHeap->size >= MAX_HEAP_SIZE) {
        printf("Heap is full, insertion failed.\n");
        return;
    }
    maxHeap->heap[maxHeap->size++] = value;
    heapifyUp(maxHeap, maxHeap->size - 1);
}

// 下移操作（向下調整堆）
void heapifyDown(MaxHeap *maxHeap, int i) {
    int maxIndex = i;
    int left = leftChild(i);
    int right = rightChild(i);

    if (left < maxHeap->size && maxHeap->heap[left] > maxHeap->heap[maxIndex]) {
        maxIndex = left;
    }
    if (right < maxHeap->size && maxHeap->heap[right] > maxHeap->heap[maxIndex]) {
        maxIndex = right;
    }

    if (i != maxIndex) {
        int temp = maxHeap->heap[i];
        maxHeap->heap[i] = maxHeap->heap[maxIndex];
        maxHeap->heap[maxIndex] = temp;
        heapifyDown(maxHeap, maxIndex);
    }
}
// 提取最大值操作
int extractMax(MaxHeap *maxHeap) {
    if (maxHeap->size <= 0) {
        printf("Heap is empty, extraction failed.\n");
        return -1;
    }
    int max = maxHeap->heap[0];
    maxHeap->heap[0] = maxHeap->heap[maxHeap->size - 1];
    maxHeap->size--;
    heapifyDown(maxHeap, 0);
    return max;
}

int main() {
    MaxHeap maxHeap;
    init(&maxHeap);

    insert(&maxHeap, 5);
    insert(&maxHeap, 3);
    insert(&maxHeap, 8);
    insert(&maxHeap, 1);

    printf("Max heap: ");
    for (int i = 0; i < maxHeap.size; i++) {
        printf("%d ", maxHeap.heap[i]);
    }
    printf("\n");
    insert(&maxHeap, 4);
    printf("Extracted max value: %d\n", extractMax(&maxHeap));

    printf("Max heap after extraction: ");
    for (int i = 0; i < maxHeap.size; i++) {
        printf("%d ", maxHeap.heap[i]);
    }
    printf("\n");

    return 0;
}
