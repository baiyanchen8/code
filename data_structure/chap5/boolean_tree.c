#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef enum {AND, OR, NOT, VAR} logic;
typedef struct node* boolean_node; 
struct node {
    logic type;
    short int value;
    boolean_node left;
    boolean_node right;
};

boolean_node c_node(logic type){
    boolean_node A=(boolean_node)malloc(sizeof(struct node));
    A->type=type;
    A->value=0;
    A->left=NULL;
    A->right=NULL;
    return A; 
}

boolean_node create_tree(char * inputs){
    boolean_node stack[100];
    int top = -1;

    for (int i = 0; inputs[i]; ++i) {
        char c = inputs[i];
        if (c == '(') {
            continue;
        } else if (c == '&' || c == '|') {
            boolean_node node = c_node(c == '&' ? AND : OR);
            stack[++top] = node;
        } else if (c == '-') {
            // 對應非運算符 '-'
            boolean_node node = c_node(NOT);
            stack[++top] = node;
        } else if (c == '0' || c == '1') {
            boolean_node node = c_node(VAR);
            node->value = c - '0';
            stack[++top] = node;
        } else if (c == ')') {
            boolean_node right = stack[top--];
            boolean_node logic = stack[top--];
            if (logic->type != NOT) {
                // 如果邏輯運算符不是非，則取出左節點
                boolean_node left = stack[top--];
                logic->left = left;
            }else{
                // ?
                logic->left = NULL;
            }
            logic->right = right;
            stack[++top] = logic;
        }
    }
    while (top > 0) {
    boolean_node right = stack[top--];
    boolean_node logic = stack[top--];
    boolean_node left = stack[top--];
    
    if (logic->type != NOT) {
        // 如果邏輯運算符不是 NOT，則設定左右節點
        logic->left = left;
        logic->right = right;
    } else {
        // 如果是 NOT 運算符，只需設定右節點
        logic->right = right;
    }

    // 將處理完畢的節點放回堆疊中
    stack[++top] = logic;
}

    return stack[0];
}

void postorderEval(struct node* head){
    if (!head) return ;
    postorderEval(head ->left);
    postorderEval(head ->right);
    switch (head -> type){
        case NOT:
            head->value = !head-> right->value;
            break;
        case OR:
            head->value =head->left->value || head -> right ->value;
            break;
        case AND:
            head->value =head->left->value && head -> right ->value;
            break; 
        case VAR:
            break;
        default:
            break;
    }
}
void printTreeStructure(boolean_node root, int level) {
    if (!root) return;

    // 打印節點值
    printf("level:%d\t",level);
    
    printf("Type: %d, Value: %d\n", root->type, root->value);

    // 遞歸打印左子樹和右子樹
    printTreeStructure(root->left, level + 1);
    printTreeStructure(root->right, level + 1);
}
int main(){
    char expr[] = "-((1)|-(0|0))";
    boolean_node root = create_tree(expr);
    printf("Tree Structure:\n");
    printTreeStructure(root, 0);
    postorderEval(root);
    printf("Result: %d\n", root->value);
    return 0;
}
