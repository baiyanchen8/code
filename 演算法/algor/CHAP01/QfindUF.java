public class QfindUF {
    
    private int [] id;

    public QfindUF (int n){
        int i;
        id =new int[n];
        for(i=0;i<n;i++){
            id [i]=i;
        }
         
    }
    public static void main(String[] args) {
         QfindUF nQfindUF=new QfindUF(20);
         System.out.println(nQfindUF.union(19));
         nQfindUF.union(19, 17);
         nQfindUF.union(17, 9);
         nQfindUF.union(19, 16);
         System.out.println(nQfindUF.union(17));
         System.out.println(nQfindUF.union(19));
         System.out.println(nQfindUF.union(16));

    }
    public int union(int p){
        return id[p];
    }
    public void union (int p,int q){
        int pid =id[p];
        int qid =id[q];
        int i;
        for(i=0;i<id.length;i++){
            if(id[i]==pid)id[i]=qid;
        }
    }
}
