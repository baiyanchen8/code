#include <stdio.h>
#include <stdlib.h>
#include <time.h>
typedef enum {False, True} bool;

struct node {
    char data;
    struct node *pointer_left;
    bool bool_left;
    struct node *pointer_right;
    bool bool_right;
};

// 函式原型宣告
struct node *inorder_next(struct node *A);
void inorder_thread(struct node *A);
void pro(struct node *A) ;
struct node * c_node(char data);
void insetleft(struct node * root ,char data);
void insetright(struct node * root ,char data);

void root_init(struct node * root){
    struct node * tmp = c_node(' ');
    tmp->pointer_right=tmp;
    tmp ->pointer_right =root;
    root->bool_left=True;
    root->bool_right=True;
    root->pointer_left=tmp;
    root->pointer_right=tmp;
    
}
int main()
{
    srand((unsigned int)time(NULL));
    struct node * root=c_node('a');
    
    printf("%c\n",root->data);
    root_init(root);
    insetright(root,'B');
    insetleft(root->pointer_right,'s');
    insetright(root,'A');
    insetright(root,'c');
    printf("inorder:");
    inorder_thread(root);
    printf("\n");

    return 0;
}

// 找出中序遍歷的下一個節點
struct node *inorder_next(struct node *A){
    struct node * tmp = A->pointer_right;
    if(A->bool_right ==False){
        while (tmp->bool_left == False){
            tmp = tmp->pointer_left;
        }
    }
    return tmp;
}

// 中序遍歷並印出結果
void inorder_thread(struct node *A){
    struct node *tmp = A;
    while (tmp->bool_left==False)
        tmp=tmp->pointer_left;
    printf("%c ", tmp->data);
    do{
        tmp = inorder_next(tmp);
        printf("%c ", tmp->data);
    } while(A != inorder_next(tmp));
}

struct node * c_node (char data){
    struct node * tmp =(struct node * )malloc (sizeof(struct node ));
    tmp->data=data;
    tmp->bool_left=False;
    tmp->bool_right=False;
    tmp->pointer_left=NULL;
    tmp->pointer_right=NULL;      
    return tmp;
}

void insetleft(struct node * root,char data){
    // 可能有問題
    struct node * left =c_node(data);
    struct node * original_left=root->pointer_left;
    // 左指
    left->bool_left=root->bool_left;
    left->pointer_left=root->pointer_left;
    root->pointer_left=left;
    // 右指      
    left->bool_right=True;
    left->pointer_right=root;
    if (root->bool_left==False){
        // orginal left 的處理
        while (original_left->bool_right==True)
            original_left=original_left->pointer_right;
        original_left->pointer_right=left;
    }
    root->bool_left=False;
}
void insetright(struct node * root , char data){
    struct node * right = c_node(data);
    right->pointer_right=root->pointer_right;
    right->bool_right=root -> bool_right;
    right->pointer_left=root;
    right->bool_left=True;
    root->bool_right=False;
    root->pointer_right=right;
    if(right->bool_right==False){
        struct node * tmp= inorder_next(right);
        tmp->pointer_left=tmp;
    }

}