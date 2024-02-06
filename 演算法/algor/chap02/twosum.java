public class twosum {
    public static int[] two(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
    
        while (left < right) {
            int sum = nums[left] + nums[right];
            if (sum == target) {
                return new int[] { left, right };
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
    
        throw new IllegalArgumentException("No two sum solution");
    }
    public static void main(String[] args) {
        twosum aTwosum=new twosum();
        int[] nums = {-1,0, 1, 2};
        int target = 0;
        int[] indices = aTwosum.two(nums, target);
        System.out.println("Indices: " + nums[0] + ", " + nums[1]);

    }
}
