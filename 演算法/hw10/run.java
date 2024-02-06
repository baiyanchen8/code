public class run extends HW10_4110056009_01{
    public static void main(String[] args) {
        HW10_4110056009_01 aa=new HW10_4110056009_01();
        int [][] a={{3,1},{4,5},{5,4},{2,11},{9,1}};
        int [][]ax=aa.bestPhone(a);
        for (int[] is : ax) {
            for (int is2 : is) {
                System.out.print(is2+" ");
            }System.out.println();
        }
    }
}
