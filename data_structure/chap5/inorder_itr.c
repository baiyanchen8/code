#include <stdio.h>
#include <stdlib.h>

// 定義節點結構
struct node {
    struct node *left;
    struct node *right;
    int data;
};

// 創建一個新節點
struct node *create_node(int data) {
    struct node *new_node = (struct node *)malloc(sizeof(struct node));
    new_node->data = data;
    new_node->left = NULL;
    new_node->right = NULL;
    return new_node;
}

// 創建另一棵測試用的樹
struct node *create_tree() {
    struct node *root = create_node(1);
    root->left = create_node(2);
    root->right = create_node(3);
    root->left->left = create_node(4);
    root->left->right = create_node(5);
    root->right->left = create_node(6);
    root->right->right = create_node(7);
    root->left->left->left = create_node(8);
    root->left->left->right = create_node(9);
    root->left->right->left = create_node(10);
    root->left->right->right = create_node(11);
    root->right->left->left = create_node(12);
    root->right->left->right = create_node(13);
    root->right->right->left = create_node(14);
    root->right->right->right = create_node(15);
    return root;
}

// 中序遍歷(遞迴)
void in_order_recursive(struct node *A){
    if(A){
        in_order_recursive(A->left); 
        printf("%d ", A->data);
        in_order_recursive(A->right);
    }
}

// 中序遍歷(迭代)
void in_order_iterative(struct node *A){
    struct node *stack[100];
    int top = -1;
    struct node *current = A;

    while (current != NULL || top != -1) {
        while (current != NULL) {
            stack[++top] = current;
            current = current->left;
        }
        current = stack[top--];
        printf("%d ", current->data);
        current = current->right;
    }
}

// 測試遞迴版本的中序遍歷函式
void test_recursive_in_order(struct node *root) {
    printf("Recursive In-order Traversal: ");
    in_order_recursive(root);
    printf("\n");
}

// 測試迭代版本的中序遍歷函式
void test_iterative_in_order(struct node *root) {
    printf("Iterative In-order Traversal: ");
    in_order_iterative(root);
    printf("\n");
}

int main() {
    // 創建一棵樹
    struct node *root = create_tree();
    
    // 測試遞迴版本的中序遍歷函式
    test_recursive_in_order(root);
    
    // 測試迭代版本的中序遍歷函式
    test_iterative_in_order(root);
    
    return 0;
}
