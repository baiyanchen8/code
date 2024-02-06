public class shell_sort {
    public static void shellSort(int[] arr,int divide) {
        int n = arr.length;
        int k=2;
        for (int gap=k-1;gap<n;k*=k) {
            for (int i = gap; i < n; i += 1) {
                int temp = arr[i];
                int j;
                for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                    arr[j] = arr[j - gap];
                }
                arr[j] = temp;
            }
            int t=-1;
            int w=0;
            for(int i :arr){
                if(i<t){
                    w=1;
                    break;
                }else{
                    t=i;
                }
            }
            if(w==0)
                return;
        }
        
    }
    public static void main(String[] args) {
        int []x={7,4,3,3,3,3,6,53,2,1};
        shellSort(x, 2);
        for(int i:x){
            System.out.print(i+" ");
        }
    }
}
