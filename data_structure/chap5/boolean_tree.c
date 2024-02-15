#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef enum {AND, OR, NOT, VAR} logic;
typedef struct node* boolean_node; 
struct node {
    logic type;
    short int value;
    // it means current value
    boolean_node left;
    boolean_node right;
};

boolean_node c_node(logic type){
    boolean_node A=(boolean_node)malloc(sizeof(boolean_node));
    A->type=type;
    A->value=0;
    A->left=NULL;
    A->right=NULL;
    return A; 
}

boolean_node create_tree(char * inputs){
    if (strlen(inputs) == 0)
        return NULL;
    
    int i;
    boolean_node stack[10];
    int top = -1;

    for (i = 0; i < strlen(inputs); i++){
        if (inputs[i] == '-'){
            // 建立 NOT 節點，將其壓入堆疊
            boolean_node not_node = c_node(NOT);
            not_node->right = stack[top];
            stack[top] = not_node;
        } else if (inputs[i] == '&') {
            // 建立 AND 節點，將其壓入堆疊
            boolean_node and_node = c_node(AND);
            and_node->right = stack[top--];
            and_node->left = stack[top--];
            stack[++top] = and_node;
        } else if (inputs[i] == '|') {
            // 建立 OR 節點，將其壓入堆疊
            boolean_node or_node = c_node(OR);
            or_node->right = stack[top--];
            or_node->left = stack[top--];
            stack[++top] = or_node;
        } else if (inputs[i] == '(') {

            int j;
            int count = 1;
            for (j = i + 1; j < strlen(inputs); j++) {
                if (inputs[j] == '(') count++;
                else if (inputs[j] == ')') count--;
                if (count == 0) break;
            }
            // 將左括號到右括號之間的部分視為一個子表達式，建立對應的樹
            stack[++top] = create_tree(inputs + i + 1);
            i = j; // 更新 i 的位置，跳過子表達式的部分
        } else if (inputs[i] == ')') {
            // 遇到右括號，彈出堆疊中的節點直到遇到對應的左括號
            while (top > 0 && stack[top]->type != VAR) {
                top--;
            }
            if (top > 0 && stack[top]->type == VAR) {
                top--; // 彈出左括號
            }
        } else {
            // 建立變數節點，將其壓入堆疊
            boolean_node var_node = c_node(VAR);
            var_node->value = inputs[i] - '0'; // 假設變數是 '0' 或 '1'
            stack[++top] = var_node;
        }
    }

    return stack[top]; // 堆疊中最後剩餘的節點即為樹的根節點
}

int main(){
    char expr[] = "((1&0)|-(0&1))";
    boolean_node root = create_tree(expr);
    
    printf("Tree created successfully!\n");
    return 0;
}
