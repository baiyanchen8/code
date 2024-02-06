public class HW06_4110056009_5 {
    public double a=0;
    public  double find_median(int[][] arrays) {
        int total = 0;
        for (int[] arr : arrays) {
            total += arr.length;
        }
        int[] marr = new int[total];
        int index = 0;
        for (int[] arr : arrays) {
            for (int num : arr) {
                marr[index++] = num;
                }
        }
        quickSort(marr, 0, marr.length - 1);
        return a;
    }
    private void quickSort(int[] arr, int left, int right) {
        if (left < right) {
            int pivotIndex = partition(arr, left, right);
            if(pivotIndex==arr.length/2){
                if(arr.length%2==0){
                    int max=0;
                    for(int i=0;i<pivotIndex;i++)
                        max=(max>arr[i])?max:arr[i];
                    a=(max+arr[pivotIndex])/2.0;
                }else{
                    a=arr[pivotIndex];
                }
            }else if(pivotIndex<arr.length/2){
                quickSort(arr, pivotIndex + 1, right);
            }else if(pivotIndex>arr.length/2){
                quickSort(arr, left, pivotIndex - 1);
            }
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
        int temp = arr[i + 1];
        arr[i + 1] = arr[right];
        arr[right] = temp;
        return i + 1;
    }
}
