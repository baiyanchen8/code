#include <stdio.h>
#include <string.h>

int main() {
    const char* s1 = "Hello, World!\n";
    char s2[20]={0};
    FILE *fop;
    fop= fopen("opcode.txt","r");
	do{
		fscanf(fop,"%s",s2);
		printf("%s ",s2);
	}while(!feof(fop));
	printf("finsh");
    return 0;
}

