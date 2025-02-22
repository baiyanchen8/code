public class HW08_4110056009_2 extends MaxLandArea{
    int[][] grid;
    int gx,gy;
    public int area(int r, int c) {
        if (r < 0 || r >= gx || c < 0 || c >= gy|| grid[r][c] == 0)
            return 0;
        grid[r][c]=0;
        return (1 + area(r+1, c) + area(r-1, c)+area(r, c-1) + area(r, c+1));
    }
    public int maxLandArea(int[][] grid) {
        this.grid = grid;
        gx=grid.length;
        gy=grid[0].length;
        int ans = 0;
        for (int r = 0; r<gx;r+=2){
            for (int c = 0; c<gy;c+=2) {
                if(grid[r][c]!=1){
                    continue;
                }
                int x=area(r, c);
                ans = ( ans > x )?ans: x ;
            }
        }
        return ans;
    }
}