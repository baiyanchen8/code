#include <stdio.h>
#include <pthread.h>
#include <string.h>
void *busy(void *ptr) {
// ptr will point to "Hi"
	pthread_t asd = pthread_self();
	printf("%lld",asd);
    puts(ptr);
    return ptr;
}
int main() {
    void * result;
    pthread_t id;
    char *asd;
    asd= (char *)malloc(20);
    memcpy(asd,"hi,mother fucker\0",19);
    pthread_create(&id, NULL, busy,asd);
    pthread_join(id, &result);
    puts("result");
    puts(result);
    printf("%lld",id);
    return 0;
    
}
