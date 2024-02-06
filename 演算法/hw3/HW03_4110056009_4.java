public class HW03_4110056009_4 extends One_0k_rock{
    public boolean[] one0k(String[] A) {
        boolean [] a;
        a= new boolean[A.length];
        for(int i=0;i<A.length;i++){
            int c=A[i].length();
            String b=A[i];
            if((b.indexOf("1")==c>>1&&b.lastIndexOf("0")==(c>>1)-1)&&(c&1)==0)  
            a[i]=true;
        }
        return a;
    }
}