public class bsearch {
    public static int binarySearch(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;
    
        while (left <= right) {
            int mid = left + (right - left) / 2;
    
            if (arr[mid] == target) {
                return mid;
            } else if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    
        return -1; // target not found
    }
    public static void main(String[] args) {
        int[] arr = {1, 3, 5, 7, 9};
        int target = 5;
        int index = binarySearch(arr, target);
        if (index != -1) {
            System.out.println("Found target "+target+" at index " + index);
        } else {
            System.out.println("Target not found");
        }
    }
}
