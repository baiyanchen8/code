#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 定義堆疊結構
typedef struct {
    int top;      // 堆疊頂部指標
    char* array;  // 存放元素的陣列
} Stack;

// 創建一個堆疊
Stack* createStack(int capacity) {
    Stack* stack = (Stack*)malloc(sizeof(Stack));
    stack->top = -1;
    stack->array = (char*)malloc(capacity * sizeof(char));
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
void push(Stack* stack, char item) {
    stack->array[++stack->top] = item;
}

// 從堆疊彈出元素
char pop(Stack* stack) {
    return stack->array[stack->top--];
}

// 取得堆疊頂部元素，不彈出
char peek(Stack* stack) {
    return stack->array[stack->top];
}

// 取得運算符的優先級
int getPrecedence(char op) {
    switch (op) {
        case '+':
        case '-':
            return 1;
        case '*':
        case '/':
            return 2;
        default:
            return 0;  // 非運算符，優先級為0
    }
}

// 中序轉後序表達式
char* infixToPostfix(char* infix) {
    int i, j;
    int len = strlen(infix);
    char* postfix = (char*)malloc((len + 1) * sizeof(char));
    Stack* stack = createStack(len);

    for (i = 0, j = 0; i < len; ++i) {
        if (isalnum(infix[i])) {
            postfix[j++] = infix[i];
        } else if (infix[i] == '(') {
            push(stack, infix[i]);
        } else if (infix[i] == ')') {
            while (!isEmpty(stack) && peek(stack) != '(') {
                postfix[j++] = pop(stack);
            }
            pop(stack);  
        } else { 
        	postfix[j++] = ' ';  // 加入空格，用來區隔不同的數字
            while (!isEmpty(stack) && getPrecedence(peek(stack)) >= getPrecedence(infix[i])) {
                postfix[j++] = pop(stack);
            }
            push(stack, infix[i]);
        }
    }

    // 將堆疊中剩餘的運算符彈出
    while (!isEmpty(stack)) {
        postfix[j++] = pop(stack);
    }

    postfix[j] = '\0';  // 在字符串末尾添加空字符
    return postfix;
}

int main() {
    char* exp = (char*)malloc(20 * sizeof(char));

    while (strncmp(exp, "exit", 4)) {
        gets(exp);
        if (strncmp(exp, "exit", 4)) {
            char* postfix = infixToPostfix(exp);
            printf("輸入表達式 %s 的後序表達式為 %s\n", exp, postfix);
            free(postfix);  // 釋放後序表達式的記憶體
        }
    }

    free(exp);  // 釋放輸入表達式的記憶體
    return 0;
}
