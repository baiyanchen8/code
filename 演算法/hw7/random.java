import java.util.Random;
public class random {
    public int[][] ran(int i) {
        int[][] a=new int[i][2];
        Random b =new Random();
        boolean[][] c=new boolean [i][i];
        for(int j=0;j<i;j++){
            int x=b.nextInt(i)+0;
            int y=b.nextInt(i)+0;
            while(c[x][y]){
                x=b.nextInt(i)+0;
                y=b.nextInt(i)+0;
            }
            c[x][y]=true;
            a[j][0]=x;
            a[j][1]=y;
        }
        return a;
    }
}
