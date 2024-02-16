#include <stdio.h>
#include <stdlib.h>
#include <time.h>
struct node {
    struct node *left;
    struct node *right;
    char data;
};

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

int count(struct node *A){
    return A ? (count(A->left) + count(A->right))+1 : 0;

}
void in(struct node *A) {
    if (A != NULL) {
        in(A->left);
        printf("%c ", A->data);
        in(A->right);
    }
}

int main(int argc, char const *argv[])
{
    srand(time(NULL));
    struct node * root=(struct node*)malloc(sizeof(struct node));
    pro(root);
    in(root);
    printf("%d",count(root));
    return 0;
}
