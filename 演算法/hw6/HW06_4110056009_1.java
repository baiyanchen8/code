public class HW06_4110056009_1 extends MedianOfArrays {
    public double find_median(int[][] arrays) {
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
        mergeSort(marr, 0, index - 1);
        return (total % 2 == 0)?(marr[total / 2 - 1] + marr[total / 2]) / 2.0:marr[total / 2];
    }
    private void mergeSort(int[] arr, int left, int right) {
        if (left >= right) {
         return;
        }
        int mid = (left + right) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
    
    private void merge(int[] arr, int left, int mid, int right) {
        int[] temp = new int[right - left + 1];
        int i = left;
        int j = mid + 1;
        int k = 0;
        while (i <= mid && j <= right) {
            if (arr[i] < arr[j]) {
                temp[k++] = arr[i++];
            } else {
                temp[k++] = arr[j++];
            }
        }
        while (i <= mid) {
            temp[k++] = arr[i++];
        }
        while (j <= right) {
            temp[k++] = arr[j++];
        }
        for (i = 0; i < temp.length; i++) {
            arr[left + i] = temp[i];
        }
    }
}
   