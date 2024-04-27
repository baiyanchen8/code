#include <stdio.h>
#include <stdlib.h>

#define maxnode 100

int** edge;
int edgesize;
int node[maxnode];
int vist[maxnode];
int low_[maxnode];
int dfn = 0;
int v2[maxnode];

void addedge(int a, int b);
int checknode(int a, int b);
int dfs(int node);
int find_articulation(int node);

int main(int argc, char const *argv[]) {
    for (int i = 0; i < 10; i++) {
        node[i] = i + 1;
    }

    addedge(1, 2);
    addedge(2, 3);
    addedge(1, 3);
    addedge(2, 4);
    addedge(2, 5);
    addedge(4, 5);
    addedge(3, 6);
    printf("Edges:\n");
    for (int i = 0; i < edgesize; i++) {
        if (edge[i] != NULL) {
            printf("%d %d\n", edge[i][0], edge[i][1]);
        }
    }

    dfs(1);

    printf("\nNodes:\n");
    for (int i = 0; i < maxnode && node[i] != 0; i++) {
        printf("%d ", node[i]);
    }
    printf("\nLow values:\n");
    for (int i = 0; i < maxnode && node[i] != 0; i++) {
        printf("%d ", low_[i]);
    }
    printf("\nVisited:\n");
    for (int i = 0; i < maxnode && node[i] != 0; i++) {
        printf("%d ", vist[i]);
    }
    printf("\n");
    find_articulation(1);
    printf("\n");
    // Free allocated memory
    for (int i = 0; i < edgesize; i++) {
        free(edge[i]);
    }
    free(edge);

    return 0;
}
int find_articulation(int node){
        v2[node]=1;
        for (int i = 0; i < edgesize; i++) {
            if (edge[i] == NULL) break;
            if ((edge[i][0] == node && v2[edge[i][1]] == 0)) {
                int below = find_articulation(edge[i][1]);
                if (below >= vist[node] &&vist[node]!=1)   {
                    printf("%d ",node);
                    return low_[node];
                }
            }  else
            if ((edge[i][1] == node && v2[edge[i][0]] == 0)) {
                int below = find_articulation(edge[i][0]);
                if (below >= vist[node] &&vist[node]!=1)   {
                    printf("%d ",node);
                    return low_[node];
                }
            } 
        }
        return low_[node];
}
int dfs(int node) {
    printf("%d ", node);
    vist[node] = ++dfn;
    int nowdfn=dfn;
    int small = dfn;
    for (int i = 0; i < edgesize; i++) {
        if (edge[i] == NULL) break;
        if ((edge[i][0] == node && vist[edge[i][1]] == 0)) {
            int below = dfs(edge[i][1]);
            if (small > below) small = below;
        } else if ((edge[i][1] == node && vist[edge[i][0]] == 0)) {
            int below = dfs(edge[i][0]);
            if (small > below) small = below;
        } else if (edge[i][1] == node || edge[i][0] == node) {
            int below = (edge[i][0] == node) ? vist[edge[i][1]] : vist[edge[i][0]];
            if (small > below&&below!=(nowdfn-1)) small = below;
        }
    }
    low_[node] = small;
    return low_[node];
}

int checknode(int a, int b) {
    if (a == 0 || b == 0) return 0;
    for (int i = 0; i < maxnode; i++) {
        if (node[i] == 0) {
            node[i] = (a == 0) ? b : a;
        }
        if (node[i] == a) a = 0;
        if (node[i] == b) b = 0;
    }
    return (a == 0 && b == 0) ? 1 : 0;
}

void addedge(int a, int b) {
    if (!checknode(a, b)) {
        printf("Warning there is an invalid pair! %d %d \n", a, b);
        return;
    }

    if (edge == NULL || edgesize == 0) {
        edgesize = 10;
        edge = (int**)malloc(edgesize * sizeof(int*));
        for (int i = 0; i < edgesize; i++) {
            edge[i] = NULL;
        }
    }

    for (int i = 0; i < edgesize; i++) {
        if (edge[i] == NULL) {
            edge[i] = (int*)malloc(2 * sizeof(int));
            edge[i][0] = a;
            edge[i][1] = b;
            return;
        }
        if ((edge[i][0] == a && edge[i][1] == b) || (edge[i][0] == b && edge[i][1] == a)) {
            return;
        }
    }

    edgesize *= 2;
    edge = (int**)realloc(edge, edgesize * sizeof(int*));
    for (int i = edgesize / 2; i < edgesize; i++) {
        edge[i] = NULL;
    }

    addedge(a, b);
}
