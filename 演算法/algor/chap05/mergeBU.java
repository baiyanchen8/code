public class mergeBU {
    public static void sort(int[] a)
   {
      int[] aux = new int[a.length];
      for(int si=1;si<a.length;si++){
        for(int low=0;low<a.length-si;low+=2*si){
            merge(a, aux, low, low+si-1,(low+si+si-1>a.length-1)?a.length-1:low+si+si-1);
        }
    }
   }
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
    private static boolean less(int a, int b) {
        return (a>b)? false:true;
    } 
    public static void main(String[] args) {
        int[]x={7,6,5,5,4,3,2,1,11,1,1,1,1};
        sort(x);
        for(int i:x)System.out.print(i+"  ");
     }
}
