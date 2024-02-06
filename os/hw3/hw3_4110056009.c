#include <stdio.h>

#include <stdlib.h>

#include <string.h>

#include <math.h>

#include <pthread.h>

#include <unistd.h>

# define MINPID 0

# define MAXPID 127

int count[100];

int c=0;

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

	printf("bitmap[0]=%u\n",(unsigned int)bitmap[0]);

	printf("bitmap[1]=%u\n",(unsigned int)bitmap[1]);

	printf("bitmap[2]=%u\n",(unsigned int)bitmap[2]);

	printf("bitmap[3]=%u\n",(unsigned int)bitmap[3]);

	printf("----------------------------------------\n");

}

int sleep1=9;

void *thread1(){

	int j=(rand()%(sleep1+1))+1;

	int i=allocate_pid();

	pthread_t thread_id = pthread_self();

    unsigned long id = (unsigned long)thread_id;

	printf("tid: %lu this is pid :%u ,wiil sleep %d sec \n",id,(unsigned int)i,j);

	sleep(j);

	release_pid(i);

	count[i]++;

	c++;

	pthread_exit(0);

}

int main(){

	while(allocate_map()==-1){}

	printf("-----------Allocating bitmap-----------\n");

	show();

	int run=0;

	while (run ==0 ){

		bitnum=0;

		int choice=0;

		int re_pid=0;

		pthread_t arr[100];

		int i,j;

		printf("(1)create a 100 thread (2)exit\n");

		printf("Please enter your choice :");

		scanf("%d",&choice);

		sleep1=10;

		switch (choice){

			case 1:

				while(allocate_map()==-1);

				show();

				for (i=0;i<100;i+=1)

					pthread_create(&arr[i],NULL,thread1,NULL);

				usleep(500000);

				show();

				if(bitmap[3]!=15){printf("finally!!\n");return 0;}

				for (i=0;i<100;i++)

					pthread_join(arr[i],NULL);

				show();

				break;



			case 2:

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

	printf("release pid :%u\n",pid);

	if (testbit(bitmap,pid)==0){

		printf("\n\nThis Pid is not allocated\n");

		printf("----------------------------------------\n");

		return;

	}

	bitmap[pid/32]=clearbit(bitmap,pid);

	bitnum-=1;

}


