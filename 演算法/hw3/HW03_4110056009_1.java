public class HW03_4110056009_1 extends One_0k_rock{
    public boolean[] one0k(String[] A) {
        boolean [] a;
        int n =A.length;
        a= new boolean[n];
        for(int i=0;i<n;i++){
            String b=A[i];
            int c=b.length();    
            if(c%2==0){
                int sum=0;
                for(int j=0;j<c;j++){
                    char x=b.charAt(j);
                    if(x=='1'&&j<c/2){
                        a[i]=false;
                        break;
                    }
                    if(x=='0')
                        sum++;
                }
                if(sum==c-sum)
                    a[i]=true;
            }else{
                a[i]=false;
            }

        }
        return a;
    }
}