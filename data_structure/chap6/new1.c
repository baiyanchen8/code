#include <stdio.h>
#include <stdlib.h>
#define num_vertex 10
int edge [num_vertex][2];
int edge_num;

int visited[num_vertex];

void dfs(int now){
    visited[now]=1;
    printf("%d",now);
    int i;
    for (i=0;i<num_vertex;i++){
        if (edge[i][0]==now && visited[edge[i][1]]!=0)
            dfs(edge[i][1]);
        if (edge[i][1]==now && visited[edge[i][0]]!=0)
            dfs(edge[i][0]);
    }
}

void bfs(int now){
    visited[now]=1;
    printf("%d",now);
    int i;
    for (i=0;i<num_vertex;i++){
        if (edge[i][0]==now && visited[edge[i][1]]!=0)
            dfs(edge[i][1]);
        if (edge[i][1]==now && visited[edge[i][0]]!=0)
            dfs(edge[i][0]);
    }
}

void add_edge(int a,int b){
    int i;
    for (i=0;i<edge_num;i++)
        if ((edge[i][0]==a&&edge[i][1]==b)||(edge[i][0]==b&&edge[i][1]==a))
            return;
    edge_num+=1;
    edge[edge_num-1][0]=a;
    edge[edge_num-1][0]=b;
}

int main(int argc, char const *argv[])
{
    /* code */
    
    return 0;
}
