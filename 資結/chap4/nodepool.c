#include <stdio.h>

// 定義節點結構
struct node {
    int data;
    struct node* next;
};

struct node* pool;

// 清空節點的函式
void erase(struct node* A) {
    struct node* tmp;
    while (A) {
        tmp = A;
        A = A->next;
        // 清除其中內容
        tmp->data=-1;
        tmp->next = pool;
        pool = tmp;
    }
}

// 取得新節點的函式
struct node* getnode() {
    if (pool) {
        struct node* tmp;
        tmp = pool;
        pool = pool->next;
        tmp->next = NULL;
        return tmp;
    } else {
        struct node* tmp;
        tmp = (struct node*)malloc(sizeof(struct node));
        tmp->next=NULL;
        return tmp;
    }
}

// 測試用的函式
void printList(struct node* head) {
    while (head) {
        printf("%d ", head->data);
        head = head->next;
    }
    printf("\n");
}

int main() {
    // 測試清空節點的函式
    struct node* head = getnode();
    head->data = 1;

    struct node* node2 = getnode();
    node2->data = 2;
    head->next = node2;

    struct node* node3 = getnode();
    node3->data = 3;
    node2->next = node3;

    printf("原始鏈表: ");
    printList(head);

    erase(head);
    head=NULL;
    printf("清空後鏈表: ");
    printList(head);

	printList(pool);
    return 0;
}

