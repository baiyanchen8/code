#include <stdio.h>

#define MAX_TERMS 101
#define MAX_COL 10

typedef struct {
	int row;
    int col;
    int value;
} Term;

void fastTranspose(Term a[], Term b[]) {
    int rowTerms[MAX_COL], startingPos[MAX_COL];

    int numCols = a[0].col;
    int numTerms = a[0].value;

    b[0].row = numCols;
    b[0].col = a[0].row;
    b[0].value = numTerms;

    if (numTerms > 0) {
    	int i;
        for ( i = 0; i < numCols; i++) {
            rowTerms[i] = 0;
        }

        for ( i = 1; i <= numTerms; i++) {
            rowTerms[a[i].col]++;
        }

        startingPos[0] = 1;

        for ( i = 1; i < numCols; i++) {
            startingPos[i] = startingPos[i - 1] + rowTerms[i - 1];
        }

        for ( i = 1; i <= numTerms; i++) {
            int j = startingPos[a[i].col]++;
            b[j].row = a[i].col;
            b[j].col = a[i].row;
            b[j].value = a[i].value;
        }
    }
}

int main() {
    Term a[MAX_TERMS] = {{6, 6, 8}, {0, 1, 15}, {0, 3, 22}, {0, 5, -15}, {1, 1, 11}, {1, 2, 3}, {2, 3, -6}, {4, 0, 9}, {5, 2, 91}};
    Term b[MAX_TERMS];

    fastTranspose(a, b);
	int i;
    printf("Original Matrix:\n");
    for ( i = 0; i <= a[0].value; i++) {
        printf("Row: %d, Col: %d, Value: %d\n", a[i].row, a[i].col, a[i].value);
    }

    printf("\nTransposed Matrix:\n");
    for ( i = 0; i <= b[0].value; i++) {
        printf("Row: %d, Col: %d, Value: %d\n", b[i].row, b[i].col, b[i].value);
    }

    return 0;
}

