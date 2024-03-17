#include <stdio.h>
#include <stdlib.h>
#define num_vertex 10
int edge[num_vertex][2];
int edge_num;
struct node {
    int data;
    struct node * next;
};
int visited[num_vertex];
struct node * queue;
struct node * tail;

void addqueue(int add){
    if (!queue){
        queue=(struct node *)malloc(sizeof(struct node));
        queue->data = add;
        queue->next = NULL; 
        tail = queue;
    }else{
        struct node * tmp = (struct node *)malloc(sizeof(struct node));
        tmp->data = add;
        tmp->next = NULL; 
        tail->next = tmp;
        tail = tmp;
    }
}

int dequeue(){
    if (!tail){
        return -1;

    }if (!queue){
        return -1;
    }
    else{
        if (tail== queue){
            int a=queue->data;
            free(queue);
            return a;
        }

        struct node * tmp = queue;
        while (tmp->next != tail&&tmp!=tail){
            tmp = tmp->next;
        }
        int tre = tail->data;
        free(tail);
        tail = tmp;
        return tre;
    }
}

void dfs(int now){
    visited[now] = 1;
    printf("%d ", now);
    int i;
    for (i = 0; i < num_vertex; i++){
        if (edge[i][0] == -1 || edge[i][1] == -1)
            continue;
        if (edge[i][0] == now && visited[edge[i][1]] == 0)
            dfs(edge[i][1]);
        if (edge[i][1] == now && visited[edge[i][0]] == 0)
            dfs(edge[i][0]);
    }
}

void bfs(int now){
    addqueue(now);
    int tmp;
    while (queue){
        tmp = dequeue();
        if (tmp ==-1){
            break;
        }
        visited[tmp] = 1;
        printf ("%d ", tmp);
        int i;
        for (i = 0; i < num_vertex; i++){
            if (edge[i][0] == -1 || edge[i][1] == -1)
                continue;
            if (edge[i][0] == tmp && visited[edge[i][1]] == 0)
                addqueue(edge[i][1]);
            if (edge[i][1] == tmp && visited[edge[i][0]] == 0)
                addqueue(edge[i][0]);
        }
    }
}

void add_edge(int a, int b){
    int i;
    for (i = 0; i < edge_num; i++){
        if ((edge[i][0] == a && edge[i][1] == b) || (edge[i][0] == b && edge[i][1] == a))
            return;
    }
    edge_num += 1;
    edge[edge_num - 1][0] = a;
    edge[edge_num - 1][1] = b;
}

void init(){
    int i;
    for (i = 0; i < num_vertex; i++){
        edge[i][0] = edge[i][1] = -1;
    }
}

void init_visit(){
    int i;
    for (i = 0; i < num_vertex; i++){
        visited[i] = 0;
    }
}

int main(int argc, char const *argv[]){
    init();
    add_edge(1, 2);
    add_edge(3, 2);
    add_edge(4, 2);
    add_edge(3, 5);

    printf("DFS :");
    init_visit();
    dfs(1);
    printf("\n");

    printf("BFS :");
    init_visit();
    bfs(1);
    printf("\n");

    return 0;
}
