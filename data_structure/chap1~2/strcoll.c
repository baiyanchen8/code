#include <stdio.h>
#include <string.h>

int main() {
    const char *str1 = "apple1213" ;
    const char *str2 = "apple";

    int result = strcoll(str1, str2);

    if (result < 0) {
        printf("%s is less than %s\n", str1, str2);
    } else if (result > 0) {
        printf("%s is greater than %s\n", str1, str2);
    } else {
        printf("%s is equal to %s\n", str1, str2);
    }

    return 0;
}

