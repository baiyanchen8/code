#include <stdio.h>
#include <stdlib.h>

// 定義節點結構
struct node {
    int data;
    struct node* next;
};

// 建立等價關係
void equivalence(int A[9][2], struct node* A1[]) {
    // 初始化節點陣列
    int i;
    for (i = 0; i < 12; i++) {
        A1[i] = NULL;
    }

    // 創建等價關係的鏈結串列
    for (i = 0; i < 9; i++) {
        struct node *tmp;

        // 將 A[i][0] 與 A[i][1] 加入彼此的鏈結串列中
        tmp = (struct node *)malloc(sizeof(struct node));
        tmp->next = A1[A[i][0]];
        tmp->data = A[i][1];
        A1[A[i][0]] = tmp;

        tmp = (struct node *)malloc(sizeof(struct node));
        tmp->next = A1[A[i][1]];
        tmp->data = A[i][0];
        A1[A[i][1]] = tmp;
    }
}


// 將元素加入陣列，避免重複
int add(int *ans, int *anssize, int addnum) {
    int i;
    for (i = 0; i < *anssize - 1; i++) {
        if (addnum == ans[i]) return -1;
    }
    (*anssize) += 1;
    ans = (int *)realloc(ans, (*anssize) * sizeof(int));
    ans[(*anssize) - 2] = addnum;
    return 0;
}


// 使用深度優先搜尋找尋等價關係中的元素
void find(int findi, struct node *A1[], int *ans, int *anssize) {
    if (!A1[findi]) {
        return;
    }
    struct node *tmp;
    int i = 1;  // 初始化 i 為 1
    for (tmp = A1[findi]; tmp->next!=NULL; tmp = tmp->next) {
        printf("%d: %d %d\n", i++, tmp->data,anssize[0]);  // 修正：加入 i++
        int t = add(ans, anssize, tmp->data);
        if (t != -1) find(tmp->data, A1, ans, anssize);
    }
    if (tmp!=NULL){
		int t = add(ans, anssize, tmp->data);
    	if (t != -1) find(tmp->data, A1, ans, anssize);
	}
	printf("%d finish \n",findi);
}

int main() {
    // 輸入的等價關係陣列
    int input[12][2] = {{0, 4}, {3, 1}, {6, 10}, {8, 9}, {7, 4}, {6, 8}, {3, 5}, {2, 11}, {11, 0}};
    struct node *seq[12];
    equivalence(input, seq);

    // 動態配置記憶體存放結果
    int *ans = (int *)malloc(sizeof(int));
    int anssize = 1;
    
    // 尋找等價關係中的元素
    find(6, seq, ans, &anssize);
    
    // 輸出結果
    int i;
    for (i = 0; i < anssize - 1; i++) {
        printf("%d ", ans[i]);
    }

    // 釋放動態配置的記憶體
    for (i = 0; i < 12; i++) {
        struct node *current = seq[i];
        while (current != NULL) {
            struct node *temp = current;
            current = current->next;
            free(temp);
        }
    }

    free(ans);

    return 0;
}

