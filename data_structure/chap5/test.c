#include <stdio.h>
#include <stdlib.h>

// 定義二元樹的節點結構
struct node {
    int key;
    struct node *left, *right;
};

// 定義修改搜尋函式
struct node *modify_search(struct node *head, int key) {
    struct node *big = head, *small = head;
    int b=0,s=0;
    if (big->key < key) {
        big = big->right;
        b++;
    }else {
        small = small->left;
        s++;
    }
    while (big && small ){
        if (big->key < key){
            b++;
            big = big->right;
            small=big;
        }
        if (small->key > key){
            s++;
            small = small->left;
            big =small;
        }
        struct node *tmp=(b>s)?big:small;
        printf("%d\n",tmp->key);
    }

    return (b>s)?big:small;
}
// 創建新節點
struct node *newNode(int item) {
    struct node *temp = (struct node *)malloc(sizeof(struct node));
    temp->key = item;
    temp->left = temp->right = NULL;
    return temp;
}

// 測試程式
int main() {
    // 創建一個複雜的二元樹
    struct node *root = newNode(10);
    root->left = newNode(5);
    root->right = newNode(15);
    root->left->left = newNode(3);
    root->left->right = newNode(8);
    root->right->left = newNode(12);
    root->right->right = newNode(18);
    root->left->left->left = newNode(1);
    root->left->left->right = newNode(4);
    root->left->right->left = newNode(7);
    root->left->right->right = newNode(9);
    root->right->left->left = newNode(11);
    root->right->left->right = newNode(13);
    root->right->right->left = newNode(16);
    root->right->right->right = newNode(20);

    // 進行測試
    int test_key = 14;
    struct node *result = modify_search(root, test_key);

    if (result != NULL) {
        printf("%d\n", result->key);
    } 
    // 釋放記憶體
    free(root);
    
    return 0;
}
