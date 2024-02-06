public class HW05_4110056009_2 extends littlebit{
    public int l_bit(int []A) {
        int k=A.length;
        int []mo=new int [k];
        int ans=0;
        mo[0]=1;
        for(int i=1;i<k;i++){
            if(A[i]>A[i-1]){
                mo[i]=mo[i-1]+1;
            }else if(A[i]==A[i-1]){
                mo[i]=mo[i-1];
            }else{
                mo[i]=1;
            }
        }
        for(int i=k-2;i>-1;i--){
            if(A[i]>A[i+1]&&mo[i]<mo[i+1]+1){
                mo[i]=mo[i+1]+1;
            }else if(A[i]==A[i+1]&&mo[i]<mo[i+1]){
                mo[i]=mo[i+1];
            }
            ans+=mo[i];
        }
        ans+=mo[k-1];
        return ans;
    }
} 