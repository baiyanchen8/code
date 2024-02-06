import java.util.Random;

public class test_random {
    public  int [] ran(int length){
        int [] a;
        Random rand = new Random();
        a= new int [length];
        for(int i=0;i<length;i++){
            a[i]=i+1;
        }
        for(int i=2;i<length;i++){
            int k=rand.nextInt(i-1);
            int t=a[i];
            a[i]=a[k];
            a[k]=t;
        }

        return a;
    }
}
