import java.util.Random;
import java.util.Arrays;
class merge implements Runnable{

    public void run(){
        if (arr.length<=1){
            return;
        }
        int leftarr[]=new int[arr.length/2];
        int rightarr[]=new int[arr.length/2];
        int mid =arr.length/2;
        leftarr = Arrays.copyOfRange(arr, 0, mid);
		rightarr = Arrays.copyOfRange(arr, mid, arr.length);
        merge left =new merge(leftarr);
        merge right =new merge(rightarr);    
        Thread lThread=new Thread(left);
        Thread rThread=new Thread(right);
        lThread.start();
        rThread.start();
        try {
            lThread.join();
            rThread.join();
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println("err");
        }
        int[]k = merge_func(left.get(),right.get());
        System.arraycopy(k, 0, arr, 0, k.length);
    }
    


    private int[] merge_func(int[] join, int[] join2) {
        int [] asd=new int[join.length+join2.length];
        int l=0;
        int r=0;
        while(l<join.length&&r<join2.length){
            if (join[l]<join2[r]){
                asd[l+r]=join[l];
                l++;
            }else{
                asd[l+r]=join2[r];
                r++;
            }
        }
        while (r<join2.length) {
            asd[l+r]=join2[r];
                r++;
        }

        while (l<join.length) {
            asd[l+r]=join[l];
                l++;
        }
        return asd;
    }


    public int[] get(){
        return arr;
    }
    int arr[];
    int ans[];
    public merge(int []arr){
        this.arr=arr;
    }
}
class merge_sort_with_thread{
    public static void main(String[] args) {
        int arr []=new int[100];
        Random rd=new Random();
        for (int i = 0; i < arr.length; i++) {
            arr[i]=i;
        }
        for (int i=99;i>-1;i--){
			int j=rd.nextInt(i+1)+1;
			int tmp=arr[i];
			arr[i]=arr[j];
			arr[j]=tmp;
		
		}
        System.out.println(":");
        for (int num : arr) {
            System.out.print(num + " ");
        }
        merge merg1e = new merge(arr);
        Thread mergeThread = new Thread(merg1e);
        mergeThread.start();

        try {
            mergeThread.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println(":");
        for (int num : merg1e.get()) {
            System.out.print(num + " ");
        }
    }
}