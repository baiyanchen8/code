#include <stdio.h>
#include <stdlib.h>

struct node
{
    struct node * left;
    struct node * right;
    int key;
};

struct node * search (struct node *head,int key);
struct node * inter_search (struct node *head,int key);
struct node * modify_search (struct node *head,int key);
void insert (struct node **head,int key);
void delete (struct node **head,int key);
void threeWayJoin(struct node *s,struct node *m,struct node *b);
struct node * twoWayJoin(struct node *s,struct node *b);
void split(struct node **tree,int key,struct node **small,struct node **mid,struct node **big);

// 層序遍歷打印二元樹
void level_order_traversal(struct node *root) {
    if (root == NULL) return;

    // 創建一個佇列來存儲待處理的節點
    struct node *queue[1000]; // 假設樹的節點數不超過 1000
    int front = 0, rear = 0;

    // 將根節點入佇列
    queue[rear++] = root;

    while (front < rear) {
        // 取出佇列頭部的節點
        struct node *current = queue[front++];
        printf("%d ", current->key);

        // 將左子節點入佇列
        if (current->left != NULL) {
            queue[rear++] = current->left;
        }

        // 將右子節點入佇列
        if (current->right != NULL) {
            queue[rear++] = current->right;
        }
    }
}

// 測試程式
int main() {
    // 創建一個空的二元樹
    struct node *root = NULL;

    // 插入一些節點
    insert(&root, 10);
    insert(&root, 5);
    insert(&root, 15);
    insert(&root, 3);
    insert(&root, 8);
    insert(&root, 12);
    insert(&root, 18);
    level_order_traversal(root);
    printf("\n");
    struct node *small;
    struct node *mid;
    struct node *big;
    split(&root,12,&small,&mid,&big);
    printf("small:");
    level_order_traversal(small);printf("\n");
    printf("mid:");
    level_order_traversal(mid);printf("\n");
    printf("big:");
    level_order_traversal(big);printf("\n");
    
    // 釋放記憶體
    // 需要寫一個釋放二元樹的函式，否則這裡會造成內存洩漏

    return 0;
}
void split(struct node **tree, int key, struct node **small, struct node **mid, struct node **big) {
    if (!(*tree)) {
        *small = NULL;
        *big = NULL;
        *mid = NULL;
        return;
    }
    
    struct node *sh, *bh, *s, *b;
    struct node *c;
    sh = (struct node *)malloc(sizeof(struct node));
    bh = (struct node *)malloc(sizeof(struct node));
    s = sh;
    b = bh;
    c = *tree;

    while (c) {
        if (key < (c->key)) {
            b->left = c;
            b = c;
            c = c->right;
        } else if (key > (c->key)) {
            s->left = c;
            s = c;
            c = c->right;
        } else {
            s->right = c->left;
            b->left = c->right;
            *small = sh->left;
            *big = bh->left;
            *mid = c;
            c->left = NULL;
            c->right = NULL;
            free(sh);
            free(bh);
            return;
        }
    }

    s->right = NULL;
    b->left = NULL;
    *small = sh->left;
    *big = bh->left;
    *mid = NULL;
    free(sh);
    free(bh);
}

void threeWayJoin(struct node *s,struct node *m,struct node *b){
    if (!s&&!b&&!m)
        return;
    m->left=s;
    m->right=b;
    level_order_traversal(m);
    printf("end\n");
}

struct node * twoWayJoin(struct node *s,struct node *b){
    if (!s && !b){
        return NULL;
    }
    struct node * m=s;
    struct node * p=s;
    while(m->right){
        p=m;
        m=m->right;
    }
    if (s!=m){
        p->right=NULL;
        threeWayJoin(s,m,b);
        return m;
    }else{
        struct node * m=b;
        while(m->left){
            m=m->left;
        }
        m->left=s;
        return b;
    }
    
}

struct node * search (struct node *head,int key){
    // time : O(h) h=logn
    // space : O(h) 因為遞迴的記憶體結構(os的東西)
    if (!head) return NULL;
    if (head->key==key) return head;
    if  (head->key<key) return search(head->right,key);
    else return search(head->left,key); 
}

struct node * inter_search (struct node *head,int key){
    // O(h) h=logn 
    // space : O(1)
    struct node * tmp=head;
    while(tmp){
        if (tmp->key==key) return tmp;
        if  (tmp->key<key) tmp=tmp->right; 
        else tmp=tmp->left;
    }
    return NULL;
}

struct node * modify_search (struct node *head,int key){
    struct node * tmp=head;
    struct node * past=NULL;
    while(tmp){
        if (tmp->key==key) return NULL;
        if  (tmp->key>key){
            past=tmp;
            tmp=tmp->left; 
        }else {
            past=tmp;
            tmp=tmp->right;
        }
    }
    return past;
}

void insert (struct node **head,int key){
    struct node * target=modify_search(*head,key);
    struct node * tmp=(struct node *)malloc(sizeof(struct node *));
    tmp->key=key;
    tmp->left=NULL;
    tmp->right=NULL;
    if (target||!*head){
        if(*head){
            if(key<target->key) target->left=tmp;
            else target->right=tmp; 
        }else{
            *head =tmp;
        }
    }
}

void delete(struct node **head, int key) {
    struct node *past = NULL;
    struct node *target = *head;
    
    // 找到要刪除的節點
    while (target) {
        if (target->key == key) {
            
            struct node *s = target->left;
            struct node *b = target->right;
            if (!past) {
                // 如果目標節點是樹的根節點
                *head = twoWayJoin(s, b);
            } else {
                // 更新目標節點的父節點的指向
                if (past->left == target) {
                    past->left = twoWayJoin(s, b);
                } else {
                    past->right = twoWayJoin(s, b);
                }
            }
            free(target);
            break;
        }
        // 移動 past 和 target 指針以繼續搜索目標節點
        past = target;
        if (target->key > key) {
            target = target->left;
        } else {
            target = target->right;
        }
    }
}