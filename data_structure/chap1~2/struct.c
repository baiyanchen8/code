typedef struct{
	char name[10];
	int age;
	float salary;
	
}example_use;
struct example_2{
	char name[10];
	int age;
	float salary;
	
};
int main(int k,char *arr[]){
	example_use asd;
	struct example_2 as2;
	asd.age =0;
	printf("%d\n",asd.age); 
	as2.salary=1.234;
	printf("%f",as2.salary); 
	return 0;
}
