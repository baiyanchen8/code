public class HW01_4110056009_1 extends ArrayData{
    
    public HW01_4110056009_1(int[] A){
        this.A=A;
    }
    public static void main(String[] args) {
        int[] A={-100,5,2222,45,666,90,87,-55,123,-88888};
        HW01_4110056009_1 test=new HW01_4110056009_1(A);
        System.out.println(test.max());
        System.out.println(test.min());
    }
    public int max(){
        int i,b=A[0];
        for (i=1;i<A.length;i++){
            if(b<A[i])
                b=A[i];
        }
        return b;
    }
    public int min(){
        int i,b=A[0];
        for (i=0;i<A.length;i++){
            if(b>A[i])
                b=A[i];
        }
        return b;
    }

}