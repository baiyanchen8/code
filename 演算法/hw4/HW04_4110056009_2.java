public class HW04_4110056009_2  extends doge_coin{
    public int doge(int A[]) {
        int b=0,s=A[0];
        for(int i=1;i<A.length*4/5;i++){
            if(A[i]<s){
                s=A[i];
                continue ;
            }
            if(b<A[i]-s)
                b=A[i]-s;

        }
        return b;
    }
}
