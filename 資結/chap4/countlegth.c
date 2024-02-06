#include <stdio.h>

// 定義節點結構
struct node {
    int data;
    struct node* next;
};

// 計算鏈表長度的函式
int countlength(struct node* A) {
    if (!A) return 0;  // 如果鏈表為空，長度為0
    struct node* tmp;
    int c = 1;  // 初始長度為1，因為 A 存在
    for (tmp = A->next; tmp != NULL && A != tmp; tmp = tmp->next) {
        c++;
    }
    return c;
}

// 測試用的函式
void printList(struct node* head) {
	struct node * tmp = head;
	printf("%d ", head->data);
	head=head ->next;
    while (head!=tmp&&head) {
        printf("%d ", head->data);
        head = head->next;
    }
    printf("\n");
}

int main() {
    // 測試計算鏈表長度的函式
    struct node* head = (struct node*)malloc(sizeof(struct node));
    head->data = 1;

    struct node* node2 = (struct node*)malloc(sizeof(struct node));
    node2->data = 2;
    head->next = node2;

    struct node* node3 = (struct node*)malloc(sizeof(struct node));
    node3->data = 3;
    node2->next = node3;
	node3->next=NULL;
    printf("原始鏈表: ");
    printList(head);

    int length = countlength(head);
    
    printf("鏈表長度: %d\n", length);

    return 0;
}

