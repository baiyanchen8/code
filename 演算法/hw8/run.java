public class run {
    public static void main(String[] args) {
        int [][] a={
            {1,1,1,1},
            {1,0,0,1},
            {1,0,0,1},
            {1,1,1,1}
        };
        rand ax= new rand();
        int x=10000,y=10000;
        HW08_4110056009_2 aa =new HW08_4110056009_2();
        HW08_4110056009_1 aaa =new HW08_4110056009_1();
        HW08_4110056009_3 aaaa =new HW08_4110056009_3();
        for (int i = 0; i < 1; i++) {
            int [][]aj =ax.ran(x,y);
            int k=aa.maxLandArea(aj);
            int j=aaa.maxLandArea(aj);
            int l=aaaa.maxLandArea(aj);
                if(k!=j||k!=l){
                    System.out.println(k+" "+l+" "+j);
                    System.out.println("error");
                }
            }
        }
    }

