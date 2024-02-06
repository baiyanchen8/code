public class run extends HW02_4110056009_1{
    public static void main(String[] args){
        long time1,time2,time3=0;
        int []n;
        n=new int[1001];
        int i;
        for(i=-500;i<=500;i++){
            n[i+500]=i;
        }
        int j=1;
        // for (i=0;i<j;i++){
            time1 = System.currentTimeMillis();
            HW02_4110056009_1 nFourSum=new HW02_4110056009_1();
            System.out.println(nFourSum.F_sum(n));
            nFourSum.F_sum(n);
            time2 = System.currentTimeMillis();
            time3+=(time2-time1);
        // }
        System.out.println(time3/j);
    }
}