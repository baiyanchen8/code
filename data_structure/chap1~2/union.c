union Data
{
   int i;
   float f;
   char  str[20];
};
 
 
 
int main(){
	union Data asd,asf;
	asd.f=1.111;
	printf("%d",asf.f);
	

}
