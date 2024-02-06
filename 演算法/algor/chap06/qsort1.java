public class qsort1 {
    public static void sort(int[] a) {
        int []aux=new int [a.length];
        sort0(a,aux,0,a.length-1);
    }
    private static void sort0(int[]a,int[]aux,int lo,int hi) {
        
        if(lo<hi)
           { int j=pratsort(a,aux,lo,hi);
                sort0(a,aux,lo,j-1);
                sort0(a,aux,j+1,hi);
            }
        else
            return;
        
        
        
    }
    private static int  pratsort(int []a,int []aux,int lo,int hi) {
        
        for(int i=lo;i<=hi;i++)aux[i]=a[i];
        int i=a[lo];
        int l=lo,h=hi;
        int j;
        for(j=lo+1;j<=hi;j++){
            if(aux[j]>i){
                a[h--]=aux[j];
            }else if(aux[j]<=i){
                a[l++]=aux[j];
            }
        }
        a[l]=i;
        return l;
    }

    public static void main(String[] args) {
        int[] a={7,8,9,4,5,6,1,2,3};

        int[] au={9,8,7,6,5,4,3,2,1};
        sort(a);
        
        for (int i : a) {
            System.out.print(" "+i);
        }
   
    }
}
