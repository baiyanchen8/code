#include <stdio.h>
#include <stdlib.h>

#define INITIAL_SIZE 5

struct Stack {
    int *arr;
    int len;
    int capacity;
};

struct Stack stack1;

void stack_init() {
    stack1.arr = (int *)malloc(INITIAL_SIZE * sizeof(int));
    stack1.len = 0;
    stack1.capacity = INITIAL_SIZE;
}

void resize_stack() {
    stack1.capacity *= 2;
    stack1.arr = (int *)realloc(stack1.arr, stack1.capacity * sizeof(int));
}

void push(int num) {
    if (stack1.len == stack1.capacity) {
        resize_stack();
    }

    stack1.arr[stack1.len++] = num;
}

void shrink_stack() {
    if (stack1.len <= stack1.capacity / 2 && stack1.capacity > INITIAL_SIZE) {
        stack1.capacity /= 2;
        stack1.arr = (int *)realloc(stack1.arr, stack1.capacity * sizeof(int));
    }
}

int pop() {
    if (stack1.len > 0) {
        int poppedElement = stack1.arr[--stack1.len];

        shrink_stack();

        return poppedElement;
    } else {
        printf("Stack underflow. Cannot pop from an empty stack.\n");
        // Return a default value (you may want to handle this differently based on your requirements)
        return -1;
    }
}

int main() {
    // Example usage
    stack_init();

    push(10);
    push(20);
    push(30);

    int poppedValue = pop();
    printf("Popped element: %d\n", poppedValue);

    poppedValue = pop();
    printf("Popped element: %d\n", poppedValue);

    // Free the allocated memory
    free(stack1.arr);

    return 0;
}

