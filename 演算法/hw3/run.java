public class run   {
    public static void main(String[] args){
        long time1,time2,time3;
        HW03_4110056009_1 A1=new HW03_4110056009_1();
        HW03_4110056009_2 A2=new HW03_4110056009_2();
        // HW03_4110056009_3 A3=new HW03_4110056009_3();
        // HW03_4110056009_4 A4=new HW03_4110056009_4();
        RandomStringGenerator aa= new RandomStringGenerator();
        long a1=0,a2=0;
        int k=1;
        for(int i=0;i<k;i++){
            String [] Text= aa.generateRandomString(10000000);
            time1 = System.currentTimeMillis();
            boolean [] a=A1.one0k(Text);
            time2 = System.currentTimeMillis();
            boolean [] b=A2.one0k(Text);
            time3 = System.currentTimeMillis();
            a1=a1+time2-time1;
            a2=a2+time3-time2;
            int w=0;
            for(int j=0;j<a.length;j++){
                if(a[j]!=b[j])
                    System.out.println(a[j]+" "+b[j]+" "+Text[j]);
            }
        }   a1/=k;a2/=k;
        
        System.out.println(a1+" "+a2);
    }
}
