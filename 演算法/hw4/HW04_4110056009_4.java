public class HW04_4110056009_4{
    public int doge(int A[]) {
        int b=0;
        int s=A[0];
        for(int i=1;i<A.length*3/5;i++){
            if(A[i]<s){
                s=A[i];
            }else  if(b<A[i]-s)
                b=A[i]-s;
        }
        return b;
    }
}