public class HW08_4110056009_3 extends MaxLandArea {
    int[][] grid;
    public int area(int r, int c) {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] == 0)
            return 0;
        grid[r][c] = 0;
        return (1 + area(r+1, c) + area(r - 1, c) + area(r, c - 1) + area(r, c + 1));
    }
    public int maxLandArea(int[][] grid) {
        this.grid = grid;
        int ans = 0;
        for (int r = 0; r < grid.length-1; r += 2) {
            for (int c = 0; c < grid[0].length-1;c+=1+grid[r][c+1]) {
                int x = area(r, c);
                ans = (ans > x) ? ans : x;
            }
        }
        return ans;
    }
}