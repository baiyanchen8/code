public class HW04_4110056009_1 extends doge_coin{
    public int doge(int A[]) {
        int b=0;
        int n=A.length;
        int s=A[0];
        for(int i=1;i<n;i++){
            if(A[i]<s){
                s=A[i];
                continue ;
            }
            if(b<A[i]-s){
                b=A[i]-s;
            }
        }
        return b;
    }
}