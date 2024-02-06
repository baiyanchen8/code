class thread1 extends Thread{
    int i;
    public thread1(){
        i=0;
    }
    public static void main(String[] args) {
        thread1 assd =new thread1();
        Thread  assThread= new Thread(assd);
        assThread.start();
        Innerthread12 assd1=new Innerthread12();
        Thread  assThread1= new Thread(assd1);
        assThread1.start();
    }
    public  void run(){
        System.out.println(i);
    }
}
/**
 * Innerthread1
 */
class Innerthread12 implements Runnable{
    int i;
    public Innerthread12(){
        i=0;
    }
    public void run(){
        System.out.println(Thread.currentThread().getName());
    }
}