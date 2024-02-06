
#include <stdio.h>
#include <stdlib.h>

struct node {
    struct node * pre;
    struct node * next;
    // 其他資料型態
    int data;
};
struct node * insert(struct node *A,int data){
	struct node *tmp=(struct node * )malloc(sizeof (struct node));
	tmp ->pre = tmp;
	tmp ->next = tmp;
	tmp->data=data; 
	if (!A){
		return tmp;
	}{
		tmp->next=A->next;
		tmp->pre=A;
		tmp->next->pre=tmp;

		A->next=tmp;   
	}
	return A;
}
void print(struct node *A){
	struct node* tmp;
	for(tmp=A->next;tmp!=A&&tmp!=NULL;tmp=tmp->next){
		printf("%d ",tmp->pre->data);
	}
	printf("%d \n",tmp->pre->data);
}
void deleter(struct node *A,struct node *target){
	struct node *past = target-> pre;
	struct node *nxt = target-> next;
	nxt->pre=past;
	past->next=nxt;
	free(target);
}
int main(){
	struct node *tmp=NULL;
	int i;
	for (i=0;i<10;i++){
		tmp = insert(tmp,i);
		printf("insert %d : \n",i);
		print(tmp);
	}
	printf("delete %d\n",tmp->next->data);
	deleter(tmp,tmp->next);
	print(tmp);
	return 0;
}
