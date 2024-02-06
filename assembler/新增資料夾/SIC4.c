#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define BOOL int
#define TRUE 1
#define FALSE 0

// there is where to place path of file

#define f_src "source.txt" 
#define f_op  "opcode.txt"
#define f_in "in.txt"
#define f_ob "ob.txt"
#define f_sym "sym.txt"
#define f_new "new.txt"

//all define size here

#define word_size 14
#define line 100

// all function
int pass1();
void pass2();
int hextodec(char*);
char* dectohex(int);


// struct 
// to save label opcode and operand
typedef struct save{
	char label[word_size], opcode[word_size], operand[word_size];
	//dec
	int location;
}element;

// to save opcode
typedef struct opcode{
	char opcode[word_size];
	//dec
	int code;
}opcode;


//all gobal variable
int nline=0;
element *savearr;
int start_adr,end_adr;
int len_of_op=0;
opcode *oparr;
int main()
{	
	char s2[word_size]={'\0'};
    char s1[word_size]={'\0'};
	// load opcode 
	int i=0;
	FILE * fop;
    fop=fopen(f_op,"r");
	if(!fop){
		printf("there is no find opcode file\n");
		exit(1);
	}
	
    rewind(fop);
    while(fgets(s1,word_size,fop)){
		len_of_op+=1;
	}
	rewind(fop);
    oparr = (opcode*)malloc(len_of_op*sizeof(opcode));
    do{
    	memset(s1, '\0', sizeof(s2));
    	memset(s2, '\0', sizeof(s1));
		fscanf(fop,"%s %s\n",s1,s2);
		strcpy(oparr[i].opcode,s1);
		oparr[i].code=hextodec(s2);
		i++;
	}while(!feof(fop));
	fclose (fop);
	
	printf("---SIC ASSEMBLER START---\n");
	printf("-----pass1 start------\n");
    pass1();
    printf("-----pass1 finish------\n");
    
	// pass2  start
	printf("-----pass2 start------\n");
    pass2();
    printf("-----pass2 finish------\n");
    printf("-----finish------\n");
    return 0;
}

int pass1(){

	FILE * fsrc;
	FILE * fin;
	FILE * fsym;
	fin=fopen(f_in,"w+");
	if(!fin){
		printf("there is no find in file\n");
		exit(1);
	}
	fsym = fopen(f_sym, "w+");
	if(!fsym){
		printf("there is no find opcode file\n");
		exit(1);
	}
	fsrc=fopen(f_src,"r");
	if(!fsrc){
		printf("there is no find source file\n");
		exit(1);
	}
	char label[word_size], opcode[word_size], operand[word_size];

	char tmp[word_size];
	char oneline[line]={0};
	int comment_line=0;
	while(fgets(oneline,50,fsrc)){
		nline+=1;
		if(strchr(oneline, '.')!=NULL){
			comment_line++;
		}
	}
	nline-=comment_line;
	savearr = (element*) malloc((nline)*(sizeof(element)));
	rewind(fsrc);
	strcpy(oneline,"");
	int i;
	for(i=0;i<nline;i++){
		
		memset(oneline, '\0', sizeof(oneline));
		memset(savearr[i].opcode, '\0',sizeof(savearr[i].opcode));
		memset(savearr[i].label, '\0',sizeof(savearr[i].label));
		memset(savearr[i].operand, '\0',sizeof(savearr[i].operand)/sizeof(char));
		memset(tmp,'\0', sizeof(tmp));
		fgets(oneline,50,fsrc);
		while(strchr(oneline, '.')!=NULL){
			memset(oneline, '\0', sizeof(oneline));
			fgets(oneline,50,fsrc);
		}
		int k=0,j=0;
		// split label ,opcode ,operand
		if (oneline[0]=='\n'){
			continue;
		}
		if (oneline[0]!='\t'){
			k=0;
			// label
			while(oneline[k]!='\t'){
					k++;
					if (oneline[k]=='\n'){
						strncpy(savearr[i].label,&oneline[0],k);
						savearr[i].operand[k-j]='\0';

						goto mark1;
					}
			}
			strncpy(savearr[i].label,&oneline[0],k);

			// opcode 
			k+=1;
			j=k;
			
			while(oneline[k]!='\t'){
					k++;
					if (oneline[k]=='\n'){
						strncpy(savearr[i].opcode,&oneline[j],k-j);
						savearr[i].operand[k-j]='\0';
						goto mark1;
					}
			}
			strncpy(savearr[i].opcode,&oneline[j],k-j);
			 // opcode 
			 k+=1;
			j=k;
			while(oneline[k]!='\t'){
					k++;
					if (oneline[k]=='\n'){
						strncpy(savearr[i].operand,&oneline[j],k-j);
						savearr[i].operand[k-j]='\0';

						goto mark1;
					}
			}
			strncpy(savearr[i].operand,&oneline[j],k-j);

			mark1 :continue;
		}else{
//   		opcode 
			j=1;
			k=1;
			while(oneline[k]!='\t'){
					k++;
					if (oneline[k]=='\n'){
						strncpy(savearr[i].opcode,&oneline[j],k-j);
						savearr[i].operand[k-j]='\0';
						goto mark2;
					}
			}
			strncpy(savearr[i].opcode,&oneline[j],k-j);
			// operand
			k++;
			j=k;
			while(oneline[k]!='\t'){
					k++;
					if (oneline[k]=='\n'){
						strncpy(savearr[i].operand,&oneline[j],k-j);
						savearr[i].operand[k-j]='\0';
						goto mark2;
					}
			}
			strncpy(savearr[i].operand,&oneline[j],k-j);
			mark2 :continue;
		}
		
	}
//	error detect duplicate symbol
//	because there is a proc name at start ,so we don't need to scan first line 
	for(i=1;i< nline;i++){
		if(strcmp(savearr[i].label,"")!=0){
			int j;
			for(j=i+1;j<nline;j++){
				if(strcmp(savearr[j].label,"")!=0){
					if(strcmp(savearr[j].label,savearr[i].label)==0){
						printf("there has a double define!!");
						exit(1);
					}
				}
			}
		}	
	}

//	error detect none exist opcode
	for(i=0;i< nline;i++){
		if(strcmp(savearr[i].opcode,"BYTE")==0||strcmp(savearr[i].opcode,"WORD")==0||strcmp(savearr[i].opcode,"START")==0){
			//	success
		}else if(strcmp(savearr[i].opcode,"RESW")==0||strcmp(savearr[i].opcode,"RESB")==0){
			//	success
		}else if(strcmp(savearr[i].opcode,"END")==0){
			break;
		}else{
			int j;
			int bool_op=0;
			for(j=0;j<len_of_op;j++){
				if(strcmp(savearr[i].opcode,oparr[j].opcode)==0){
						bool_op=1;
				}
			}
			if(bool_op==0){
				//opcode none exist 
				printf("opcode not exist!!");
				exit(1);
			}
		}	
	}
	
	
//	location

	for( i=0;i<nline;i++){
		if(i==0){
			if(strcmp(savearr[i].opcode,"START")==0){
				int integer;
				if(strcmp(savearr[i].operand,"")==0){
					// if  no operand
					 integer=0;
				}else{
					 integer = hextodec(savearr[i].operand);
				}
				
	//			use decimal to store location
				savearr[i].location=integer;
	//			use hex to output location
	
				fprintf(fin,"%s\t%s\t%s\t%s\n",dectohex(savearr[i].location),savearr[i].label,savearr[i].opcode,savearr[i].operand);
	
				savearr[++i].location=integer;
				fprintf(fin,"%s\t%s\t%s\t%s\n",dectohex(savearr[i].location),savearr[i].label,savearr[i].opcode,savearr[i].operand);
				start_adr=integer;
				continue;
			}else{
				// no start
				savearr[0].location=0;
				fprintf(fin,"%s\t%s\t%s\t%s\n","0",savearr[i].label,savearr[i].opcode,savearr[i].operand);
				start_adr=0;
				continue;
			}
		}else if(strcmp(savearr[i].opcode,"END")==0){
			// there is end
			if(strcmp(savearr[i-1].opcode,"BYTE")==0){				
				int len =0,j;
				for (j=2;j<word_size;j++){
					if(savearr[i-1].operand[j]=='\''){
						len=j-2;
						break;
					}
				}
				if(savearr[i-1].operand[0]=='C'){
					savearr[i].location=savearr[i-1].location+len;
				}else if (savearr[i-1].operand[0]=='X'){
						savearr[i].location=savearr[i-1].location+(len+1)/2;
				}else{
					printf("there is no \"%c\" type of byte!! ",savearr[i-1].operand[0]);
					exit(0);
				}
				
				
			}else if(strcmp(savearr[i-1].opcode,"RESW")==0&&i>1){
				savearr[i].location=savearr[i-1].location+3*atoi(savearr[i-1].operand);
			}else if (strcmp(savearr[i-1].opcode,"RESB")==0&&i>1){
				savearr[i].location=savearr[i-1].location+atoi(savearr[i-1].operand);
			}else{
				savearr[i].location=savearr[i-1].location+3;	
			}
			end_adr=savearr[i].location;
			
			fprintf(fin,"\t\t%s\t%s\n",savearr[i].opcode,savearr[i].operand);
			
			break;
		}else{
			if (i>0){
				if(strcmp(savearr[i-1].opcode,"BYTE")==0){				
					int len =0,j;
					for (j=2;j<word_size;j++){
						if(savearr[i-1].operand[j]=='\''){
							len=j-2;
							break;
						}
					}
					if(savearr[i-1].operand[0]=='C'){
						savearr[i].location=savearr[i-1].location+len;
					}else if (savearr[i-1].operand[0]=='X'){
							savearr[i].location=savearr[i-1].location+(len+1)/2;
					}
				}else if(strcmp(savearr[i-1].opcode,"RESW")==0&&i>1){
					savearr[i].location=savearr[i-1].location+3*atoi(savearr[i-1].operand);
				}else if (strcmp(savearr[i-1].opcode,"RESB")==0&&i>1){
					savearr[i].location=savearr[i-1].location+atoi(savearr[i-1].operand);
				}else{
					savearr[i].location=savearr[i-1].location+3;	
				}
			}
			fprintf(fin,"%s\t%s\t%s\t%s\n",dectohex(savearr[i].location),savearr[i].label,savearr[i].opcode,savearr[i].operand);
		}
		
	}
	int start=nline +1 ;
//	 sym table
	for( i =0 ;i< nline ; i++){
		if(strcmp(savearr[i].label,"") && strcmp(savearr[i].opcode,"START")!=0){
			if(savearr[i].location!=0){
				fprintf(fsym,"%s\t%s\n",dectohex(savearr[i].location),savearr[i].label);
			}else{
				fprintf(fsym,"%s\t%s\n","0",savearr[i].label);
			}
			
		}
	}
	
	fclose(fsrc); 
	fclose(fin);
	fclose(fsym);
	return 0;
}

void pass2(){
	int i,location,objlen=0,tmp_adr=0;
	int textnum=1;
	char text_per_line[12*word_size];
	strcpy(text_per_line,"");
	FILE * fobj;
	fobj=fopen(f_ob,"w");
    
	for (i=0;i<nline;i++){
		
		if(i==0){
			if(strcmp(savearr[i].opcode,"START")==0){
				// start opcode
				int obj_length=end_adr-start_adr;
				fprintf(fobj, "H%-6s%06s%06X\n", savearr[i].label, savearr[i].operand , obj_length);
				textnum=0;
				continue;
			}else{
				int obj_length=end_adr-start_adr;
				textnum=0;
				fprintf(fobj, "H%-6s%06s%06X\n","\t", "0000" , obj_length);
				continue;
			}
		}else if(strcmp(savearr[i].opcode,"END")==0){ 
			// end opcode
			fprintf(fobj, "%02X",strlen(text_per_line)/2);
			fprintf(fobj, "%s", text_per_line);
			int start_adr_from_end;
			int j;
			for(j=0;j<nline;j++){
				if(strcmp(savearr[i].operand,savearr[j].label)==0){
					start_adr_from_end=savearr[j].location;
					break;
				}	
			}
			
			fprintf(fobj, "\nE%06X\n", start_adr_from_end);
			
			break;
			
		} else if(strcmp(savearr[i].opcode,"BYTE")==0){
			// byte opcode
			int len =0,j;
			int objcode=0;
			if (savearr[i].operand[0]=='C'){
				// byte c mode charater
				for (j=2;j<word_size;j++){
					if(savearr[i].operand[j]=='\''){
						len=j-2;
						break;
					}
					objcode = objcode*0x100 + savearr[i].operand[j];
				}
				char temp[len*2];
				sprintf(temp, "%06X", objcode);
				strncat(text_per_line, temp, len*2);
				objlen += len;
				
			}else if (savearr[i].operand[0]=='X'){
				// byte x mode hex mode
				char hex[word_size] = "";
				for (j=2;j<word_size;j++){
					if(savearr[i].operand[j]=='\''){
						len=j-2;
						break;
					}
				}
				strncat(hex,&savearr[i].operand[2],len);
				char temp[len*2];
				objcode = hextodec(hex);
				objlen=(len+1)/2;
				strncat(text_per_line, hex, len);
			} 
		}else if (strcmp(savearr[i].opcode,"WORD")==0){
			// word opcode
			int objcode;
			objcode =atoi(savearr[i].operand);
			objlen += 3;
			char temp[6];
			sprintf(temp, "%06X", objcode);
			strncat(text_per_line, temp, 6);
		}else if(strcmp(savearr[i].opcode,"RESB")==0||strcmp(savearr[i].opcode,"RESW")==0){
			// do nothing
		}else{
			BOOL find_op =FALSE,find_sym=FALSE,X=FALSE;
			// other opcode
			int n_op=0;
			int operand_adr=0;
			int j;
			for(j=0;j<len_of_op;j++){
				if(strcmp(savearr[i].opcode,oparr[j].opcode)==0){
					find_op=TRUE;
					n_op=j;

					break;
				}	
			}
			if(!find_op){
				if(savearr[i].opcode[4]-0==32){
					printf("yes");
				}
			}
			if(strcmp(savearr[i].operand,"")!=0){
				if(find_op==TRUE){
					for(j=0;j<strlen(savearr[i].operand);j++){
							if(savearr[i].operand[j]=='X'&&savearr[i].operand[j-1]==','){
								X=TRUE;
								break;
						}
					}
					char op[word_size]={'\0'};
					if (X){
						
						for(j=0;j<strlen(savearr[i].operand);j++){
							if(savearr[i].operand[j]=='X'&&savearr[i].operand[j-1]==','){
								strncpy(op,savearr[i].operand,j-1);
								break;
							}
						}
						for(j=0;j<nline;j++){
							if(strcmp(op,savearr[j].label)==0){
								find_sym=TRUE;
								operand_adr=savearr[j].location;
								break;
							}
						}
					}else{
						strcpy(op,savearr[i].operand);
						for(j=0;j<nline;j++){
							if(strcmp(savearr[i].operand,savearr[j].label)==0){
								find_sym=TRUE;
								operand_adr=savearr[j].location;
								break;
							}	
						}
					}
					// if symbol not exist
					if(find_sym==FALSE){
						printf("can't find symbol %s",op);
						exit(1);
					} 
						
				}
				
			}else{
				operand_adr=0;
			}
			
			int te =oparr[n_op].code*0x10000 + X*0x8000 + operand_adr;
			
			objlen+=3;
			char tmp[6]={'\0'};
			sprintf(tmp,"%06X", te);
			strncat(text_per_line, tmp, 6);
			// end of other
		} 
		
		if (textnum==0){
			fprintf(fobj, "T%06X",savearr[i].location);
			tmp_adr=savearr[i].location;
		}
		textnum++;
		if(textnum==10){
			fprintf(fobj, "%02X",strlen(text_per_line)/2);
			fprintf(fobj, "%s\n",text_per_line);

			textnum=0;
			objlen=0;
			strcpy(text_per_line,"");
		}}	
	fclose(fobj);
} 
int hextodec(char* hexString) {
    int length = strlen(hexString);
    int decimal = 0;
	int i;
    for (i = 0; i < length; i++) {
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
	int i;
    // Convert decimal to hexadecimal
    for (i = numDigits - 1; i >= 0; i--) {
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
