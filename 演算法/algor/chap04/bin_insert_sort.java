
import java.util.Arrays;

public class bin_insert_sort {
    public static int binarySearch0(int[] a, int fromIndex, int toIndex,int key) {
        int low = fromIndex;
        int high = toIndex -1;

        while (low <= high) {
            int mid = (low + high) >>> 1;
            int midVal = a[mid];

            if (midVal < key)
                low = mid + 1;
            else if (midVal > key)
                high = mid - 1;
            else{
                while(a[mid]==a[mid+1])mid++;
                return mid; 
            }
                
        }
        if(key!=a[a.length-1]){
            return -low -1;
        }
        return -low-2;
    }
    public static void bin_insert_sort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];
            int j = Math.abs(binarySearch0(arr, 0, i, key) + 1);
            System.arraycopy(arr, j, arr, j+1, i-j);
            // source,formsourceindex,destination,todestinationindex,copynum
            arr[j] = key;
            for(int k=0;k<arr.length;k++){
                System.out.print(" "+arr[k]);
            }System.out.println();
        }
    }
    public static void main(String[] args) {
        int []a={-1,1,2,3,4};
        int i=binarySearch0(a,0,a.length,5);
        System.out.println(i);
        
        if(i>=0){
            System.out.println((a.length-i-1));
            
        }else{
            System.out.println(a.length+i+1);
        }
    }
}