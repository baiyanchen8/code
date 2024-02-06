public class HW06_4110056009_2 extends MedianOfArrays {
    
    public double find_median(int[][] arrays) {
        double a=0;
        int length=0;
        int siw,limit1;
        int max=arrays[0][0],min=arrays[0][0];
        for (int[] arr : arrays) {
            max=(max>arr[arr.length-1])?max:arr[arr.length-1];
            min=(min<arr[0])?min:arr[0];
            length+=arr.length;
        }
        siw=length&1;
        limit1=length>>>1;
        if(siw==1){
            a+=midfound(min, max, arrays,limit1+1);
        }else if(siw==0){
            a+=midfound(min, max, arrays,limit1);
            a+=midfound(min, max, arrays,limit1+1);
            a*=0.5;
        }
       return a;
    }
    private  int midfound (int min,int max,int [][]arrays,int limit){
        int start = min, end = max,mid;	
		while (start+1 < end) {
			mid = (start + end) >>> 1;
			if (check(arrays, mid) >= limit) 
				start = mid;
			else 
				end = mid;
		}		
		if (check(arrays, end) >= limit)
			return end;
		return start;
    }
    private int check(int[][] arrays,int num){
        int mid=num;
        int big=0;
        for(int [] arr:arrays){
            if(arr[0]>mid){
                big+=arr.length;
           }else if(arr[arr.length-1]<mid){
           }else 
            big+=bin(arr,mid);
        }
        return big;
    }
    private int bin(int[] array, int target) {
		int start = 0, end = array.length-1, mid;
		while (start+1 < end) {
			mid = (start + end) >>> 1;
			if (array[mid] >= target)
				end = mid;
			else
				start = mid;
		}
		if (array[start] >= target)
			return array.length - start;
		if (array[end] >= target)
			return array.length - end;
		return 0;
	}
}
