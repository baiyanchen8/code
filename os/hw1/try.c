#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
# define MINPID 0
# define MAXPID 128
int main(){
	int A[4]={0};
	int x=0,y=1,z=0;
	while(z<=31){
		z+=1;
		x+=y;
		y*=2;
		
	}
	int k=2;
	printf("%d",(A[(k/32)]|(1<<(k%32))));
	return (A[(k/32)]|(1<<(k%32)));
}
