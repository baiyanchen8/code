public class HW02_4110056009_5 extends FourSum{
    public int F_sum(int[] A) {
        int n=A.length-1;
        int s=0;
        int i,j;
        Q(A,0,n);
        for (i=0;i<n-2;i++) {
            if(A[i]+A[i+1]+A[i+2]+A[i+3]>0)break;
            for (j=i+1;j<n-1;j++) {
                if(A[i]+A[j]+A[j+1]+A[j+2]>0)break;
                int l=j+1,r=n;
                while (l<r) {
                    int t=A[i]+A[j]+A[l]+A[r];
                    if(t==0){
                        s++;
                        l++;
                        r--;
                    }else if(t>0){
                        r--;
                    }else{
                        l++;
                    }
                }
            }
        }
        return s;
    }
    public void Q(int[] a,int l,int r) {
        if (l<r) {
            int p = partition(a, l, r);
            Q(a,l,p-1);
            Q(a,p+1,r);
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