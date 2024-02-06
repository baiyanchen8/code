public class HW01_4110056009_2 extends ArrayData{
    
    public HW01_4110056009_2(int[] A){
        this.A=A;
    }
    public static void main(String[] args) {
        int[] A={-100,5,2222,45,666,90,87,-55,123,-88888};
        HW01_4110056009_2 test=new HW01_4110056009_2(A);
        System.out.println(test.max());
        System.out.println(test.min());
    }
    public int max(){
        int i;
        for (i=1;i<A.length;i++){
            if(A[0]<A[i])
                A[0]=A[i];
            
        }
        return A[0];
    }
    public int min(){
        int i;
        for (i=1;i<A.length;i++){
            if(A[0]>A[i])
                A[0]=A[i];
        }
        return A[0];
    }

}