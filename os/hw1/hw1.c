#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
# define MINPID 0
# define MAXPID 127

int bitmap[4]={0};
int bitnum=0;
int allocate_map(void);
int allocate_pid(void);
void release_pid(int pid);
int setbit(int A[],int k){
	int l =A[(k/32)]|(1<<(k%32));
	return l;
}
int clearbit(int A[],int k){
	return A[k/32]&~(1<<(k%32));
}
int testbit(int A[],int k){
	int tmp = A[(k/32)]&(1<<(k%32));
	tmp=tmp>>(k%32); 
	return tmp;
}
void show(){
	printf("bitmap[0]=%d\n",bitmap[0]);
	printf("bitmap[1]=%d\n",bitmap[1]);
	printf("bitmap[2]=%d\n",bitmap[2]);
	printf("bitmap[3]=%d\n",bitmap[3]);
	printf("----------------------------------------\n");
}
int main(){
	
	while(allocate_map()==-1){}
	printf("-----------Allocating bitmap-----------\n");
	show();
	int run=0;
	while (run ==0 ){
		
		int choice=0;
		int re_pid=0;
		int i,j;
		printf("(1)create a process (2)delete a process (3)exit\n");
		printf("Please enter your choice :");
		scanf("%d",&choice);
		
		switch (choice){
			case 1:
				i=allocate_pid();
				switch (i){
					case -1:
						printf("fail to allocated bit!\n");
						break;
					default:
						printf("Sussful to allocated PID,the new PID of process: %d\n",i);
						break;
				}
				show();
				break;
			case 2:
				printf("Please enter the pid you want to delete :");
				scanf("%d",&re_pid);
				release_pid(re_pid);
				break;
			case 3:
				run=1;
				printf("Exit this process!");
				return 0;

			default :
				printf("you input the wrong choice!! try again\n");
				printf("----------------------------------------\n");
				break;
		}
		
		
	}

}
int allocate_map(void){
	int i=0;
	for (i=0;i<4;i++){
		if(bitmap[i]!=0){
			return -1;
		} 
		bitmap[i]=0;
	}
	return 1;
}
int allocate_pid(void){
	if (bitnum>MAXPID){
		return -1;
	}
	int i =0;
	for (i =0 ;i<=MAXPID;i++){
		if(testbit(bitmap,i) == 0){
			bitmap[i/32]=setbit(bitmap,i);
			bitnum+=1;
			return i; 
		}
	}
	return -1;
}
void release_pid(int pid){
	if (testbit(bitmap,pid)==0){
		printf("\n\nThis Pid is not allocated\n");
		printf("----------------------------------------\n");
		return;
	}
	bitmap[pid/32]=clearbit(bitmap,pid);
	bitnum-=1;
	show();
}
