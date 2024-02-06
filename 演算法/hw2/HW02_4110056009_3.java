public class HW02_4110056009_3 extends FourSum{
    public int [] A1;
    public int F_sum(int[] A) {
        A1=A;
        int n = A1.length,i,j;
        int sum=0;
        quickSort(A1, 0, n-1);
        for (i = 0; i < n-3&&A1[i]<0;i++) {
            for (j = i + 1; j < n - 2; j++) {
                int left = j + 1, right = n - 1;
                while (left < right) {
                    int total = A1[i] + A1[j] + A1[left] + A1[right];
                    if (total==0) {
                        left++;
                        right--;
                        sum=sum+1;
                    }if(total>0){
                        right--;
                    }if(total<0){
                        left++;
                    }
                }
            }
            
        }
        return sum;
    }
    public void quickSort(int[] arr, int left, int right) {
        if (left < right) {
            int pivot = partition(arr, left, right);
            quickSort(arr, left, pivot - 1);
            quickSort(arr, pivot + 1,right);
        }
    }
    private int partition(int[] arr, int left, int right) {
        int pivot = arr[right];
        int i = left - 1;
        for (int j = left; j < right; j++) {
            if (arr[j] < pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        int temp = arr[i+1];
        arr[i+1] = arr[right];
        arr[right] = temp;
        return i + 1;
    }

}