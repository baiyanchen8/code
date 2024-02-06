public class insertion_sort {
    private int []arr;
    public insertion_sort(int []arrary){
        arr=arrary;
        int i,j,k;
        for(i=0;i<arr.length;i++){
            for(j=i;j>0;j--){
                if(arr[j]<arr[j-1]){
                    k=arr[j-1];
                    arr[j-1]=arr[j];
                    arr[j]=k;
                }else{
                    break;
                }
            }
        }
    }
    public String toString(){
        String x=new String("");
        for(int i=0;i<arr.length;i++){
            x=x.concat(" "+arr[i]);
        }
        
        return x;
    }
    public static void main(String[] args) {
        int []x={7,6,5,4,3,2,1};
        insertion_sort a=new insertion_sort(x);
        System.out.println(a);
    }
}