
import java.util.Random;

public class knuth_shuffle {
    public static void main(String[] args) {
        for(int i:shuffle(10)){
            System.out.print(" "+i);
        }
    }
    public static void swap(int[] arr,int i,int j){
         int t=arr[i];
         arr[i]=arr[j];
         arr[j]=t;
    }
    public static int[] shuffle(int len){
        Random rand = new Random();
        int []x=new int [len];
        x[0]=1;
        for(int i=1;i<len;i++){
            x[i]=i+1;
            swap(x,i,rand.nextInt(i));
        }
        return x;
    }
    
}
