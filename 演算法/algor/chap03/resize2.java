public class resize2 {
    public static void main(String[] args) {
        resize2 arr=new resize2(2);
        arr.add(0, 0);
        arr.add(1);
        System.out.println(arr);
    }
    private int[] a;
    private int len=0;
    public resize2(int []arrary,int length){
        a=new int [length];
        for(int i=0;i<arrary.length;i++){
            a[i]=arrary[i];
        }
        len=arrary.length;
    }
    public resize2(int length){
        a=new int [length];
        for(int i=0;i<length;i++){
            a[i]=0;
        }
        len=-1;
    }
    public void add(int index,int num){
        if(len==-1){
            a[0]=num;
            len++;
            if(len>a.length/2)resize();
            return;
        }
        if(index>len) System.exit(2);
        int temp=num;
        len++;if(len>a.length/2)resize();
        for(int i=index;i<len;i++){
            i=temp;
            temp=a[i+1];
        }
    }
    public void add(int num){
        if(len==-1){
            len++;if(len>a.length/2)resize();
            a[len]=num;
            return;
        }
        int temp=num;
        len++;  if(len>a.length/2)resize();
        a[len]=num;
    }
    public void resize(){
        int x=a.length;
        int[] b=new int[2*x];
        for(int i=0;i<x;i++){
            b[i]=a[i];
        }
        a=b;
    }
    public String toString()
	{
		String x=new String(""); ;
        for(int i=0;i<len+1;i++){
            x=x.concat(" "+a[i]);
        }
        return x;	
	}
}