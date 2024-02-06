#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cstdlib>
#include <math.h>

// there is where to place path of file

#define f_src "./source.txt" 
#define f_op  "opcode.txt"
#define f_in "intermediate.txt"
#define f_ob "object.txt"
#define f_sym "symbol_table.txt"
#define f_new "new.txt"

//all define size here

#define word_size 10
#define line 100

// all file here
FILE * fsrc;
FILE * fop;
FILE * fin;
FILE * fsym;
FILE * fnew;
FILE * fobj;


// all function
int pass1();
void pass2();
int hextodec(char*);
char* dectohex(int);
typedef struct save{
	char label[word_size], opcode[word_size], operand[word_size];
	//dec
	int objectcode;
	int location;
}element;
typedef struct opcode{
	char opcode[word_size];
	//dec
	int code;
}opcode;
//all gobal variable
static element *savearr;
static opcode *oparr;

int main()
{	
	int i=0,nline=0;
	char s2[word_size]={'\0'};
    char s1[word_size]={'\0'};
	printf("---SIC ASSEMBLER START---\n");
	fsrc=fopen(f_src,"r");
	if(!fsrc){
		printf("there is no find source file\n");
		exit(1);
	}
	fop=fopen(f_op,"r");
	if(!fsrc){
		printf("there is no find opcode file\n");
		exit(1);
	}
	fin=fopen(f_in,"w+");
	fsym = fopen(f_sym, "w+");
	fnew=fopen(f_new,"w");
	
	
    int k=pass1();
    printf("-----pass1 finish------\n");
    // load opcode 
    
    
    rewind(fop);
    while(fgets(s1,word_size,fop)){
		nline+=1;
	}
	rewind(fop);
    oparr = (opcode*)malloc(nline*sizeof(opcode));
    do{
    	memset(s1, '\0', sizeof(s2));
    	memset(s2, '\0', sizeof(s1));
		fscanf(fop,"%s %s\n",s1,s2);
		strcpy(oparr[i].opcode,s1);
			oparr[i].code=hextodec(s2);
		i++;
	}while(!feof(fop));
//    pass2();
	fclose(fop);
	fclose(fsrc);
	fclose(fin);
	fclose(fsym);
	fclose(fnew);
    free(oparr);
    printf("-----finish------\n");
    return 0;
}

int pass1(){
	char label[word_size], opcode[word_size], operand[word_size];
	char temp=EOF;
	char tmp[word_size];
	char oneline[line]={0};
	int nline=0;
	
	while(fgets(oneline,50,fsrc)){
		nline+=1;
	}
	savearr = (element*) malloc(nline*(sizeof(element)));
	rewind(fsrc);
	
	for(int  i=0;i<nline;i++){
		memset(oneline, '\0', sizeof(oneline));
		memset(savearr[i].opcode, '\0',sizeof(savearr[i].opcode));
		memset(savearr[i].label, '\0',sizeof(savearr[i].label));
		memset(savearr[i].operand, '\0',sizeof(savearr[i].operand)/sizeof(char));
		memset(tmp,'\0', sizeof(tmp));
		fgets(oneline,30,fsrc);
		int tab_num=0;
		// split label ,opcode ,operand
		for(int j=0;j<30 ;j++){
			if(oneline[j]=='\n'||oneline[j]==EOF){
				break;
			}
			if(oneline[j]!='\t'&&j==0){
				//it means that label  exist
				int k=j;
				while(oneline[k]!='\t'){
					k++;
				}
				strncpy(savearr[i].label, oneline+j,k-j);
			}
			if(oneline[j]=='\t'&&j==0&&tab_num==0){
				//it means that label dosn't exist
				int k=j+1;
				while(oneline[k]!='\t'&& oneline[k] != '\n'){
					k++;
				}
				strncpy(savearr[i].opcode, oneline+j+1,k-j-1);
				tab_num++;
				j=k+1;
				memset(tmp,'\0', sizeof(savearr[i].operand));
//				load string to tmp 
				strcpy(tmp,oneline+j);

//				it remove all \n after tmp 
				if(strlen(tmp)!=0){
					strncpy(label,tmp,(strlen(tmp)-1));
				}
//				it move string to operand 
				k=j;
				while(oneline[k]!='\t'&& oneline[k] != '\n'&&oneline[k]-0!=32){
					k++;
				}
				strncpy(savearr[i].operand, oneline+j,k-j);
				break;
			}else if(oneline[j]=='\t'&&tab_num==0&&j!=0) {
				//it means that  opcode exist 
				int k=j+1;
				while(oneline[k]!='\t'&& oneline[k] != '\n'){
					k++;
				}
				strncpy(savearr[i].opcode, oneline+j+1,k-j-1);
				tab_num++;
				j=k+1;
				k=j;
				while(oneline[k]!='\t'&& oneline[k] != '\n'&&oneline[k]-0!=32&&oneline[k] != 'X'){
					k++;
				}
				strncpy(savearr[i].operand, oneline+j,k-j);
				break;
			}
		}
		
	}
//	location
	for(int i=0;i<nline;i++){
		if(strcmp(savearr[i].opcode,"START")==0){
			
			int integer = hextodec(savearr[i].operand);
//			use decimal to store location
			savearr[i].location=integer;
//			use hex to output location
			fprintf(fin,"%s\t%s\t%s\t%s\n",dectohex(savearr[i].location),savearr[i].label,savearr[i].opcode,savearr[i].operand);
			
			savearr[++i].location=integer;
		}else if(strcmp(savearr[i].opcode,"END")==0){
			
			fprintf(fin,"\t\t%s\t%s\t%s\n",savearr[i].label,savearr[i].opcode,savearr[i].operand);
			
			break;
		}else{
			if(strcmp(savearr[i].opcode,"RESW")==0){
				savearr[i].location=savearr[i-1].location+3*atoi(savearr[i].operand);
			}else if (strcmp(savearr[i].opcode,"RESB")==0){
				savearr[i].location=savearr[i-1].location+atoi(savearr[i].operand);
			}else{
				savearr[i].location=savearr[i-1].location+3;	
			}
		}
		fprintf(fin,"%s\t%s\t%s\t%s\n",dectohex(savearr[i].location),savearr[i].label,savearr[i].opcode,savearr[i].operand);
	
	}
	int start=nline +1 ;
	// sym table
	for(int i =0 ;i< nline ; i++){
		if(strcmp(savearr[i].label,"") && i > start){
			fprintf(fsym,"%s\t%s\n",savearr[i].label,dectohex(savearr[i].location));
		}else if (strcmp(savearr[i].opcode,"START")==0){
			start=i;
		}
	}
	
	return 0;
}

void pass2(){
	//undo
	
}

int hextodec(char* hexString) {
    int length = strlen(hexString);
    int decimal = 0;

    for (int i = 0; i < length; i++) {
        char currentChar = hexString[i];

        // Convert hex character to decimal value
        int digit;
        if (currentChar >= '0' && currentChar <= '9') {
            digit = currentChar - '0';
        } else if (currentChar >= 'A' && currentChar <= 'F') {
            digit = currentChar - 'A' + 10;
        } else if (currentChar >= 'a' && currentChar <= 'f') {
            digit = currentChar - 'a' + 10;
        } else {
            printf("Invalid hex string! %s \n",hexString);
            return 0;
        }

        // Calculate the decimal value
        decimal += digit * pow(16, length - i - 1);
    }

    return decimal;
}
char* dectohex(int decimal) {
    // Determine the number of digits required
    int temp = decimal;
    int numDigits = 0;
    while (temp != 0) {
        temp /= 16;
        numDigits++;
    }

    // Allocate memory for the hexadecimal string
    char* hexString = (char*)malloc((numDigits + 1) * sizeof(char));
    if (hexString == NULL) {
        printf("Memory allocation failed!\n");
        return NULL;
    }

    // Convert decimal to hexadecimal
    for (int i = numDigits - 1; i >= 0; i--) {
        int remainder = decimal % 16;

        // Convert remainder to hexadecimal character
        if (remainder < 10) {
            hexString[i] = remainder + '0';
        } else {
            hexString[i] = remainder - 10 + 'A';
        }

        decimal /= 16;
    }

    // Add null terminator
    hexString[numDigits] = '\0';

    return hexString;
}
