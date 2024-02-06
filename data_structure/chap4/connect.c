
#include <stdio.h>
#include <stdlib.h>

struct node {
    struct node* next;
    int data;
};
struct node* connect(struct node* P1, struct node* P2) {
    if (!P1) return P2;
    if (!P2) return P1;

    struct node* tmp;
    for (tmp = P1; tmp->next != NULL; tmp = tmp->next);

    tmp->next = P2;
    return P1;
}

void printlink(struct node* poly) {
    while (poly) {
        printf("%d ", poly->data);
        poly = poly->next;
    }
    printf("\n");
}
// 函數用於生成包含一串 link list 的結構
struct node* generateLinkedList(int size) {
    struct node* head = NULL;
    struct node* current = NULL;

    // 生成 link list，包含數字 1 到 size
    int i;
    for (i = 1; i <= size; ++i) {
        // 創建新節點
        struct node* newNode = (struct node*)malloc(sizeof(struct node));
        if (!newNode) {
            // 記憶體分配失敗，處理錯誤
            printf("Memory allocation failed!\n");
            exit(EXIT_FAILURE);
        }

        // 設定節點的資料
        newNode->data = i;
        newNode->next = NULL;

        // 將新節點加入 link list
        if (!head) {
            // 若 link list 為空，將新節點設為頭節點
            head = newNode;
            current = head;
        } else {
            // 若 link list 不為空，將新節點連接到目前節點的後面
            current->next = newNode;
            current = newNode;
        }
    }

    // 返回 link list 的頭指標
    return head;
}
int main (){
	struct node * tmp =generateLinkedList(3);
	printlink(tmp);
	struct node * tmp1 =generateLinkedList(5);
	printlink(tmp1);
	printlink(connect(tmp,tmp1));
}
