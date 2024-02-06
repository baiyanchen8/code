import java.util.ArrayList;
public class timsort {
    private static void merge(int[] a, int[] aux, int lo, int mid, int hi){
        for (int k = lo; k <= hi; k++) aux[k] = a[k];

        int i = lo, j = mid+1;
        for (int k = lo; k <= hi; k++){
            if (i > mid)
            a[k] = aux[j++];
            else if (j > hi)
            a[k] = aux[i++];
            else if (less(aux[j], aux[i])) 
            a[k] = aux[j++];
            else
            a[k] = aux[i++];
        }

    }

   public static void sort(int[] a)
   {
      int[] aux = new int[a.length];
    
      int mid=1,hi=0,mi=0;
      while(a[mid]>=a[mi]){
        mid++;
        mi++;
      }
      hi=mi+1;
      while(hi<a.length){
        int hh=hi+1;
        while(a[hh]>=a[hi]&&hh<a.length){
            if(hh==a.length-1){
                hi++;
                break;
            }
            hi++;
            hh++;
        }
        merge(a, aux, 0,mi,hi);
        mi=hi;
        hi++;
      }
   }

    private static boolean less(int a, int b) {
        return (a>b)? false:true;
    } 
     public static void main(String[] args) {
        int[]x={1,2,3,2,4,5,1,2,3};
        sort(x);
        for(int i:x)System.out.print(i+"  ");
     }
}
