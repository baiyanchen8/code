#include <stdio.h>
#include <string.h>

int main() {
    const char *stringA = "Hello, World!";
    const char *stringB = "x";

    char *result = strstr(stringA, stringB);

    if (result != NULL) {
        printf("'%s' 在 '%s' 中的位置：%ld\n", stringB, stringA, result - stringA);
    } else {
        printf("'%s' 不是 '%s' 的子串\n", stringB, stringA);
        if (result ==NULL){
        	printf("yess");
		}
    }

    return 0;
}

