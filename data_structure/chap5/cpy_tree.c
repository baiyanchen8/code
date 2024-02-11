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

struct node * copy_tree(struct node *original){
    if (!original) return NULL;
    struct node * head=(struct node * )malloc(sizeof(struct node *));
    head->data= original->data;
    head -> left = copy_tree(original->left);
    head -> right = copy_tree(original->right);
    return head;
}
int equal_tree(struct node *A,struct node * B){
    return (!A&&!B)||(A->data==B->data
    &&equal_tree(A->left,B->left)
    &&equal_tree(A->right,B->right));
}
int main(int argc, char const *argv[])
{
    struct node *head=create_tree();
    struct node *tmp =copy_tree(head);
    printf("%d\n",equal_tree(head,tmp));
    return 0;
}
