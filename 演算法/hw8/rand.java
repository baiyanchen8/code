import java.util.Random;
public class rand {
    int[][] ran(int x,int y) {
        int [][]re=new int[x][y];
        Random aa=new Random();
        for (int i =0;i<x;i++) {
            for (int j=0;j<y;j++) {
                re[i][j]=aa.nextInt(2);
            }
        }
        return re;
    }
}