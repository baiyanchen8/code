#include <stdio.h>
#include <stdlib.h>

// 定義堆疊結構
typedef struct {
    int top;      // 堆疊頂部指標
    int* array;   // 存放元素的陣列
} Stack;

// 創建一個堆疊
Stack* createStack(int capacity) {
    Stack* stack = (Stack*)malloc(sizeof(Stack));
    stack->top = -1;
    stack->array = (int*)malloc(capacity * sizeof(int));
    return stack;
}

// 判斷堆疊是否滿
int isFull(Stack* stack, int capacity) {
    return stack->top == capacity - 1;
}

// 判斷堆疊是否空
int isEmpty(Stack* stack) {
    return stack->top == -1;
}

// 將元素壓入堆疊
void push(Stack* stack, int item) {
    stack->array[++stack->top] = item;
}

// 從堆疊彈出元素
int pop(Stack* stack) {
    return stack->array[stack->top--];
}

// 計算後序表達式，支援空格分隔的輸入
int evaluatePostfixWithWhitespace(char* exp) {
    int i;
    Stack* stack = createStack(strlen(exp));
    if (!stack)
        return -1;  // 分配記憶體失敗

    for (i = 0; exp[i]; ++i) {
        // 跳過空格
        if (isspace(exp[i]))
            continue;

        // 處理數字
        if (isdigit(exp[i])) {
            int num = 0;
            while (isdigit(exp[i])) {
                num = num * 10 + (exp[i] - '0');
                ++i;
            }
            --i;  // 因為迴圈會再加一次，所以減回去
            push(stack, num);
        } else {
            // 處理運算符，從堆疊彈出兩個數字進行計算，再將結果壓回堆疊
            int val1 = pop(stack);
            int val2 = pop(stack);
            switch (exp[i]) {
            case '+': push(stack, val2 + val1); break;
            case '-': push(stack, val2 - val1); break;
            case '*': push(stack, val2 * val1); break;
            case '/': push(stack, val2 / val1); break;
            }
        }
    }
    return pop(stack);  // 堆疊頂部即為計算結果
}

// 主函式，接受使用者輸入並進行後序表達式的計算
int main() {
    char *exp = malloc(20);  // 分配記憶體用來存放使用者輸入
    printf("規則 \n1. 輸入數字\n2. 輸入運算符時請加上空格分隔\n   例如：12 3+7* -> (12+3)*7\n3. 輸入 exit 可結束程式\n");
    
    while (strncmp(exp, "exit", 4)) {
        gets(exp);
        if (strncmp(exp, "exit", 4))
            printf("輸入表達式 %s 的計算結果為 %d\n", exp, evaluatePostfixWithWhitespace(exp));
    }

    return 0;
}
