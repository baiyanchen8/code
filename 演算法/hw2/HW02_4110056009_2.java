public class HW02_4110056009_2 extends FourSum{
    public int F_sum(int[] A1) {
        int n = A1.length-1,i, j,sum=0;
        quickSort(A1, 0, n);
        for (i = 0; i < n-2&&A1[i]<0; i++) {
            for (j = i + 1; j < n - 1&&A1[i]+A1[j]<0; j++) {
                int left = j + 1, right = n ;
                while (left<right) {
                    int total = A1[i] + A1[j] + A1[left] + A1[right];
                    if (total==0) {
                        sum++;
                        left++;
                        right--;
                    }else if(total>0){
                        right--;
                    }else{
                        left++;
                    }
                }
            }
        }
        return sum;
    }
    private void quickSort(int[] arr, int left, int right) {
        if (left < right) {
            int pivot = partition(arr, left, right);
            quickSort(arr, left, pivot - 1);
            quickSort(arr, pivot + 1,right);
        }
    }
    private int partition(int[] arr, int left, int right) {
        int pivot = arr[right];
        int i = left - 1,temp;
        for (int j = left; j < right; j++) {
            if (arr[j] < pivot) {
                i++;
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        temp = arr[i+1];
        arr[i+1] = arr[right];
        arr[right] = temp;
        return i + 1;
    }
}