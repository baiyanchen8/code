#include <stdio.h>
#include <stdlib.h>

// 定義邊的結構
struct Edge {
    int src, dest, weight;
};

// 比較函數，用於 qsort 排序邊的權重
int compare(const void *a, const void *b) {
    return ((struct Edge*)a)->weight - ((struct Edge*)b)->weight;
}

// 查找函數，用於查找節點的根節點
int find(int parent[], int i) {
    if (parent[i] == -1)
        return i;
    return find(parent, parent[i]);
}

// Union 函數，用於合併兩個集合
void Union(int parent[], int x, int y) {
    int xroot = find(parent, x);
    int yroot = find(parent, y);
    parent[xroot] = yroot;
}

// 使用 Kruskal 演算法生成最小生成樹
void KruskalMST(struct Edge edges[], int V, int E) {
    struct Edge result[V];
    int e = 0;
    int i = 0;
    qsort(edges, E, sizeof(edges[0]), compare); // 根據權重對邊進行排序

    int *parent = (int*) malloc(V * sizeof(int)); // 創建用於查找的父節點陣列
    for (int v = 0; v < V; ++v)
        parent[v] = -1; // 初始化每個節點的父節點為 -1

    while (e < V - 1 && i < E) {
        struct Edge next_edge = edges[i++];
        int x = find(parent, next_edge.src);
        int y = find(parent, next_edge.dest);
        if (x != y) {
            result[e++] = next_edge;
            Union(parent, x, y);
        }
    }

    printf("Following are the edges in the constructed MST\n");
    for (i = 0; i < e; ++i)
        printf("%d -- %d == %d\n", result[i].src, result[i].dest, result[i].weight);
    free(parent); // 釋放父節點陣列的記憶體
}

int main() {
    int V = 20; // 節點數量
    int E = 20; // 邊數量
    struct Edge edges[] = {
        {11, 1, 12}, {1, 2, 3}, {2, 4, 6}, {3, 6, 9}, {4, 8, 12}, {5, 10, 15},
        {6, 12, 18}, {7, 14, 21}, {8, 16, 24}, {9, 18, 27}, {10, 20, 30},
        {11, 10, 21}, {12, 24, 36}, {13, 26, 39}, {14, 28, 42}, {15, 30, 45},
        {16, 13, 29}, {17, 7, 24}, {18, 36, 54}, {19, 4, 23}
    };

    KruskalMST(edges, V, E);
    return 0;
}
