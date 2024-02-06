public class HW03_4110056009_3 extends One_0k_rock{
    public boolean[] one0k(String[] A) {
        boolean [] a;
        int n =A.length;
        a= new boolean[n];
        for(int i=0;i<n;i++){
            int c=A[i].length();    
            if(c%2==0){
                int w=0;
                char[] b=A[i].toCharArray();
                for(int j=0;j<c/2;j++){
                    char x=b[j],y=b[c-j-1];
                    if((x=='1')||(y=='0')){
                        a[i]=false;
                        w=1;
                        break;
                    }
                }
                if(w==0)
                    a[i]=true;
            }else{
                a[i]=false;
            }
        }
        return a;
    }
}