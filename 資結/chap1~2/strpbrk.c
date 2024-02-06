#include <stdio.h>
#include <string.h>

int main() {
    const char *str = "Hello, World!";
    const char *chars_to_search = "aeiou";

    char *result = strpbrk(str, chars_to_search);

    if (result != NULL) {
        printf("Found character: %c\n", *result);
    } else {
        printf("No characters found.\n");
    }

    return 0;
}

