public class topdownmerge {
   private static void merge(int[] arr, int left, int mid, int right) {
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
     

   public static void sort(int[] a)
   {
      int aux[]=new int[a.length];
      mergeSort(a, 0, a.length-1);
   }
   private static void mergeSort(int[] arr, int left, int right) {
      if (left >= right) {
       return;
      }
      int mid = (left + right) / 2;
      mergeSort(arr, left, mid);
      mergeSort(arr, mid + 1, right);
      merge(arr, left, mid, right);
  }
    private static boolean less(int a, int b) {
        return (a>b)? false:true;
    } 
     public static void main(String[] args) {
        int[]x={7,3,1};
        sort(x);
        for(int i:x)System.out.print(i+"  ");
     }
}
