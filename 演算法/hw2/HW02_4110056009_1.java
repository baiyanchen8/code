public class HW02_4110056009_1 extends FourSum{
    class e1_9{
        public int data,d1,d2;
        public e1_9(int data,int d1,int d2){
            this.data=data;
            this.d1=d1;
            this.d2=d2;
        }
    }
    public int F_sum(int[] A1) {
        int sum=0,i,j,n=A1.length,left,right,target;
        int n1=n*(n-1)/2,t=0;
        e1_9[] A=new e1_9[n1];
        for (i=0;i<n-1;i++){
            for(j=i+1;j<n;j++){
                A[t++]=new e1_9(A1[i]+A1[j],A1[i],A1[j]);
            }
        }
        quickSort(A, 0,t-1);
        for(i=0;i<n1&&A[i].data<0;i++){
                target=A[i].data*-1;
                left=i+1;right=n1-1;
                while(left<right-1){
                    int mid =(left+right)/2;
                    if(A[mid].data==target){
                        while(A[mid].data==A[mid-1].data){
                            mid--;
                        }
                        while(A[mid].data==target){
                            if(A[mid].data==target&A[i].d1!=A[mid].d1&&A[i].d2!=A[mid].d2&&A[i].d1!=A[mid].d2&&A[i].d2!=A[mid].d1)
                                sum++;
                            mid++;
                        }
                        break;
                    }else if(A[mid].data>target){
                        right=mid;
                    }else{
                        left=mid;
                    }
                }
                if(A[right].data==target&&A[right].data!=A[right-1].data)
                    if(A[i].d1!=A[right].d1&&A[i].d2!=A[right].d2)
                    if(A[i].d1!=A[right].d2&&A[i].d2!=A[right].d1)
                        sum++; 
        }
        for(i=i;i<n1&&A[i].data==0;i++)
            for(j=i+1;j<n1&&A[j].data==0;j++)
                if(A[i].d1!=A[j].d1&&A[i].d2!=A[j].d2&&A[i].d1!=A[j].d2&&A[i].d2!=A[j].d1)
                    sum++;
        return sum/3;
    }
    public void quickSort(e1_9[] arr, int left, int right) {
        if (left < right) {
            int pivot = partition(arr, left, right);
            quickSort(arr, left, pivot - 1);
            quickSort(arr, pivot + 1,right);
        }
    }
    private int partition(e1_9[] arr, int left, int right) {
        int pivot = arr[right].data;
        int i = left - 1;
        for (int j = left; j < right; j++) {
            if (arr[j].data < pivot) {
                i++;
                e1_9 t;
                t=arr[i];
                arr[i]=arr[j];
                arr[j]=t;
            }
        }
        e1_9 t;
        t=arr[i+1];
        arr[i+1]=arr[right];
        arr[right]=t;
        return i + 1;
    }
    
}