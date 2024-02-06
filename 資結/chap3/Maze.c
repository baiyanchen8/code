#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
# define maxx 10 
# define maxy 10 

int maze[maxx][maxy] = {
    {1, 0, 1, 0, 0, 0, 0, 0, 0, 0},
    {1, 0, 1, 1, 1, 1, 1, 1, 1, 0},
    {1, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {1, 1, 1, 1, 1, 1, 1, 1, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 1, 1, 1, 1, 1, 1, 1, 1, 1},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    {0, 1, 1, 1, 1, 1, 1, 1, 1, 1},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
};

// 起點和終點坐標
int start[2] = {0, 1};
int end[2] = {9, 9};

int find(int nowx, int nowy) {
    if (nowx < 0 || nowx >= maxx || nowy < 0 || nowy >= maxy || maze[nowx][nowy] == 1||maze[nowx][nowy] == 2)
        return 0;
    if (nowx == start[0] && nowy == start[1]) {
        printf("(%d, %d)\n", nowx, nowy);
        return 1;
    }
    maze[nowx][nowy] = 2;
    if (find(nowx + 0, nowy - 1)||find(nowx - 1, nowy + 0)||find(nowx + 0, nowy + 1)|| find(nowx + 1, nowy + 0)){
    	printf("(%d, %d)\n", nowx, nowy);
    	maze[nowx][nowy] = 0;
    	return 1; 
	}
    maze[nowx][nowy] = 0;
    return 0;
}

int main() {
    printf("找到的路徑：\n");
    find(end[0], end[1]);
    return 0;
}

