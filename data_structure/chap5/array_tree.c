#include <stdio.h>
#include <stdlib.h>

int find_kid(int parent){
    return (parent+1)*2-1;
}
int find_P(int kid){
    kid-=kid%2;
    return kid/2;
}
int main (int arg,char *args[]){
    int n=atoi(args[1]);
    int t =atoi(args[2]);
    int j=atoi(args[3]);
    int tree[n];
    for (int i=0;i<n;i++){
        tree[i]=i+1;
    }
    printf("parent %d, kid %d %d \n",tree[t],tree[find_kid(t)],tree[find_kid(t)+1]);
    printf("kid %d, parent  %d \n",tree[j],tree[find_P(j)]);
    return 0;
}