#include <stdio.h>
#include <stdlib.h>

// 建立等價關係
void equivalence(int A[9][2], int A1[12]) {
    int i;
    int class_num = 0;

    // 初始化 A1 陣列
    for (i = 0; i < 12; i++) {
        A1[i] = -1;
    }

    // 遍歷等價關係陣列 A
    for (i = 0; i < 9; i++) {
        // 如果兩個節點都還沒有被分類
        if (A1[A[i][0]] == -1 && A1[A[i][1]] == -1) {
            A1[A[i][0]] = class_num;
            A1[A[i][1]] = class_num++;
        } else if (A1[A[i][0]] == -1 && A1[A[i][1]] != -1) {
            // 如果 A[i][0] 還沒有被分類，但 A[i][1] 已經被分類
            A1[A[i][0]] = A1[A[i][1]];
        } else if (A1[A[i][0]] != -1 && A1[A[i][1]] == -1) {
            // 如果 A[i][0] 已經被分類，但 A[i][1] 還沒有被分類
            A1[A[i][1]] = A1[A[i][0]];
        } else if (A1[A[i][0]] != -1 && A1[A[i][1]] != -1) {
            // 如果兩個節點都已經被分類，但分類不同，則統一分類
            if (A1[A[i][0]] != A1[A[i][1]]) {
                int j;
                for (j = 0; j < 12; j++) {
                    if (A1[j] == A1[A[i][0]]) {
                        A1[j] = A1[A[i][1]];
                    }
                }
            }
        }
    }
}

int main() {
    // 輸入的等價關係陣列
    int input[12][2] = {{0, 4}, {3, 1}, {6, 10}, {8, 9}, {7, 4}, {6, 8}, {3, 5}, {2, 11}, {11, 0}};
    int un[12];

    // 呼叫 equivalence 函式
    equivalence(input, un);

    // 輸出結果
    int i;
    for (i = 0; i < 12; i++) {
        printf("%d %d \n", i, un[i]);
    }

    return 0;
}

