#include <stdio.h>
#include <stdlib.h>

// 定義節點結構
struct node {
	struct node *next;
	int data;
};

// 定義全域變數 stack，用來表示堆疊頂端
struct node *stack;

// 函式原型宣告
void push(int data);
int pop();

// 主函式
int main() {
	stack = NULL; // 初始化堆疊，設為空
	push(1);
	push(2);
	push(3);
	printf("%d \n",pop());
	printf("%d \n",pop());
	printf("%d \n",pop());
	printf("%d \n",pop());
	return 0;
}

// push 函式，將資料壓入堆疊
void push(int data) {
	if (!stack) {
		// 如果堆疊為空，則建立新節點作為堆疊頂端
		stack = (struct node *)malloc(sizeof(struct node));
		stack->data = data;
		stack->next = NULL;
	} else {
		// 如果堆疊非空，則建立新節點，並將其連接到堆疊頂端
		struct node *tmp;
		tmp = (struct node *)malloc(sizeof(struct node));
		tmp->data = data;
		tmp->next = stack;
		stack = tmp;
	}
}

// pop 函式，從堆疊中彈出資料
int pop() {
	if (!stack) {
		// 如果堆疊為空，回傳 NULL（表示無法彈出）
		return NULL;
	} else {
		// 如果堆疊非空，取得頂端節點的資料，並將頂端節點釋放
		struct node *tmp = stack->next;
		int t1 = stack->data;
		free(stack);
		stack = tmp;
		return t1;
	}
}

