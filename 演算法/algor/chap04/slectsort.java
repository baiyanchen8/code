public  class slectsort {
    private int[] arr;
    public slectsort(int [ ]a) {
        int i,k,min,length=a.length;
        for(i=0;i<length;i++){
            min=i;
            for(k=i+1;k<length;k++){
                if(a[k]<a[min])
                        min=k;
            }
            int t=a[i];
            a[i]=a[min];
            a[min]=t;   
        }
        arr=a;
    }
    public String toString(){
        String x=new String("");
        for(int i=0;i<arr.length;i++){
            x=x.concat(" "+arr[i]);
        }
        
        return x;
    }
    public static void main(String[] args) {
        int []x={4,5,3,2,1};
        slectsort a=new slectsort(x);
        System.out.println(a);
    }
}
