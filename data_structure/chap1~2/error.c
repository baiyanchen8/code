#include <stdio.h>
#include <setjmp.h>

jmp_buf exception_buffer;

void handle_error() {
    printf("An error occurred.\n");
}

int divide(int a, int b) {
    if (b == 0) {
        longjmp(exception_buffer, 1); // Jump to the setjmp point with a non-zero value
    }
    return a / b;
}

int main() {
    if (setjmp(exception_buffer) == 0) {
        // Normal execution
        int result = divide(10, 0);
        printf("Result: %d\n", result);
    } else {
        // Handle the exception
        handle_error();
    }

    return 0;
}

