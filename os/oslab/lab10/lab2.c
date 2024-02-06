#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <string.h>
#include <signal.h>
#include  <stdio.h>
#include  <signal.h>

void al(){
	printf("this is 1 :how are you\n");
	//exit(0);
}
void a2(){
	printf("this is 2 :i'm fine\n");
	//exit(0);
}
int k=0;
void alarm_handler(){
	if(k==0)
		signal(SIGINT,a2);
	else
		signal(SIGALRM,SIG_DFL);
	k++;
	alarm(3);
}
int main(){
	signal(SIGALRM,alarm_handler);
	alarm(3);
	signal(SIGINT,al);
	while (1) {
        // Your main program logic can be placed here
        // (This is just a placeholder since the original code didn't have any main logic)
    }	
	signal(SIGINT,SIG_DFL);
}
