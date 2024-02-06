#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

struct term {
    int col;
    int row;
    int value;
};

struct term *transpose(const struct term *A) {
    struct term *B = (struct term *)malloc((A[0].value + 1) * sizeof(struct term));
    B[0].value = A[0].value;
    B[0].row = A[0].col;  
    B[0].col = A[0].row;
    if (A[0].value > 0) {
        int i, j, k;
        k = 1;
        for (i = 0; i < A[0].col; i++) {
            for (j = 1; j < A[0].value + 1; j++) {
                if (A[j].col == i) {
                    B[k].value = A[j].value;
                    B[k].col = A[j].row;
                    B[k].row = A[j].col;
                    k++;
                }
            }
        }
    }
    return B;
}

int main() {
    struct term matrix[10 + 1];
    int i = 0;
    matrix[0].col = 3;matrix[0].row = 3;matrix[0].value = 3;
    matrix[1].col = 0;matrix[1].row = 2;matrix[1].value = 0;
    matrix[2].col = 1;matrix[2].row = 1;matrix[2].value = 1;
    matrix[3].col = 2;matrix[3].row = 0;matrix[3].value = 2;

    for (i = 0; i < matrix[0].value + 1; i++) {
        printf("r:%d c:%d v:%d\n", matrix[i].row, matrix[i].col, matrix[i].value);
    }

    struct term *X = transpose(matrix);

    printf("\n");

    for (i = 0; i < X[0].value + 1; i++) {
        printf("r:%d c:%d v:%d\n", X[i].row, X[i].col, X[i].value);
    }

    free(X);

    return 0;
}

