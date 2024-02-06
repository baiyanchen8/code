public class run {
    public static void main(String[] args) {
        
        int test[];
        // int []test={7,6,9,3,2,1};
        test_random t = new test_random();
        long t1,t2,t3=0,t4=0;
        int w1=0,w2=0;
        int k=1000;
        test =t.ran(100000);
        HW04_4110056009_1 A1=new HW04_4110056009_1();
        HW04_4110056009_5 A2=new HW04_4110056009_5();
        for(int i=0;i<k;i++){
            
            t1=System.currentTimeMillis();
            int j=A1.doge(test);
            t2=System.currentTimeMillis();
            t3=t2-=t1;
            
            t1=System.currentTimeMillis();
            int l=A2.doge(test);
            t2=System.currentTimeMillis();
            t4=t2-=t1;
            if(t3>t4){
                w1++;
            }
            if(t4>t3){
                w2++;
            }
            if(j!=l){
               System.out.println(l+" "+j);
            }
        }
        
        System.out.println(k+" "+w1+" "+w2);
    }
}
