#include <stdio.h>
#include <stdlib.h>

// 稀疏矩陣節點結構
struct node {
    int row;
    int col;
    int value;
    struct node *down;
    struct node *right;
};
struct outter{
	// imformation of matrix
	int row;
	int col;
	int value;
	struct node ** colum; 
	struct node ** roww;  
};
// 建立稀疏矩陣
struct outter createSparseMatrix(int rows, int cols, int data[][3], int size) {
   struct outter ans;
   ans.col=cols;
   ans.row=rows;
   ans.value=size;
   ans.colum =(struct node ** )malloc((ans.col)*sizeof(struct node*));
   ans.roww =(struct node ** )malloc((ans.row)*sizeof(struct node*));

   int i;
    for (i = 0; i < ans.col; ++i) {
        ans.colum[i] = NULL;
    }
    for (i = 0; i < ans.row; ++i) {
        ans.roww[i] = NULL;
    }

    for(i = 0; i < size; i++) {
        // 創建新節點
		struct node* new1 =(struct node * )malloc(sizeof(struct node));
		new1->row = data[i][0];
		new1->col = data[i][1];
		new1->value = data[i][2];
		new1->down = NULL;
		new1->right = NULL;

		// 插入到列
		struct node *tmp;
		if (!ans.colum[data[i][1]]) {
			ans.colum[data[i][1]] = new1; 
		} else {
			for (tmp = ans.colum[data[i][1]]; tmp->right != NULL 
			&& tmp->right->row < new1->row; tmp = tmp->right);
			new1->right = tmp->right;
			tmp->right = new1;
		} 

		// 插入到行
		if (!ans.roww[data[i][0]]) {
			ans.roww[data[i][0]] = new1; 
		} else {
			for (tmp = ans.roww[data[i][0]]; tmp->down != NULL 
			&& tmp->down->col < new1->col; tmp = tmp->down);
			new1->down = tmp->down;
			tmp->down = new1;
		} 
	}
	
    return ans;
}
int findi(struct outter matrix,int i,int j){
	struct node *tmp =matrix.colum[i];
	if (!tmp){
		return 0;
	}else{
		for(tmp =matrix.colum[i];tmp!=NULL&&tmp->row!=j;tmp=tmp->right);
		 if (!tmp){
		 	return 0;
		 }else{
		 	return tmp->value;
		 }
	}
}
void printmatrix(struct outter matrix ){
	int i,j;
	for (i=0;i<matrix.col;i++){
		for (j=0;j<matrix.row;j++){
			printf("%d ",findi(matrix,i,j));
		}
		printf("\n");
	}
}
void freematrix(struct outter matrix){
	int i,j;
	for (i=0;i<matrix.col;i++){
		struct node *tmppast,*now;
		for (tmppast=matrix.colum[i];tmppast!=NULL;){
			now=tmppast->right;
			free(tmppast);
			tmppast=now;
		}
	}
}
int main() {
    int data[][3] = {
        {0, 1, 3},
        {1, 2, 5},
        {2, 0, 2},
        {2, 2, 8}
    };

   struct outter sparseMatrix = createSparseMatrix(3, 3, data, sizeof(data) / sizeof(data[0]));

    printf("稀疏矩陣的表示：\n");
	printmatrix(sparseMatrix);
	freematrix(sparseMatrix);
    return 0;
}

