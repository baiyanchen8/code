#include <stdio.h>
#include <stdlib.h>

int main() {
    // 使用malloc分配一?整型??
    int *arr = (int *)malloc(5 * sizeof(int));
    int j;
    for(j=0;j<5;j++){
	
		*(arr+j)=0;
	}
	*arr=1;
    if (arr == NULL) {
        fprintf(stderr, "?存分配失?\n");
        return 1;
    }

   
    int *new_arr = (int *)realloc(arr, 10 * sizeof(int));

    if (new_arr == NULL) {
        fprintf(stderr, "重新分配存失\n");
        free(arr);  
        return 1;
    }
	for(j=0;j<10;j++){
	
		printf("%d  ",*(new_arr+j));
	}
	printf("\n");
    // 在?里可以使用new_arr

    // 最后?放?存
    free(new_arr);

    return 0;
}

