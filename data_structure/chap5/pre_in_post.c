#include <stdio.h>
#include <stdlib.h>
#include <time.h>

struct node {
    struct node *left;
    struct node *right;
    char data;
};

// 生成隨機節點的資料
void pro(struct node *A) {
    if (A != NULL) {
        // 產生隨機數並將其轉換為字母 'a' 到 'z' 之間的字元
        A->data = 'a' + rand() % 26;

        // 遞迴呼叫 pro() 函式以處理左子樹和右子樹
        if (rand()%2==1){
            A->left=(struct node *)malloc(sizeof(struct node));
            pro(A->left);
        }else{
            A->right==NULL;
        }
        if (rand()%2==1){
            A->right=(struct node *)malloc(sizeof(struct node));
            pro(A->right);
        }else{
            A->right==NULL;
        }
    }
}

// 中序遍歷樹
void in(struct node *A) {
    if (A != NULL) {
        in(A->left);
        printf("%c ", A->data);
        in(A->right);
    }
}

// 前序遍歷樹
void pre(struct node *A) {
    if (A != NULL) {
        printf("%c ", A->data);
        pre(A->left);
        pre(A->right);
    }
}

// 後序遍歷樹
void post(struct node *A) {
    if (A != NULL) {
        post(A->left);
        post(A->right);
        printf("%c ", A->data);
    }
}

// 顯示樹的形狀及內容
void show(struct node *A) {
    printf("Inorder (中序): ");
    in(A);
    printf("\nPreorder (前序): ");
    pre(A);
    printf("\nPostorder (後序): ");
    post(A);
    printf("\n");
}

int main() {
    // 初始化隨機數種子
    srand(time(NULL));

    // 創建樹的根節點
    struct node *head = (struct node *)malloc(sizeof(struct node));
    if (head == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    // 設置根節點的資料
    pro(head);

    // 顯示樹的形狀及內容
    show(head);

    // 釋放動態分配的記憶體
    free(head);

    return 0;
}
