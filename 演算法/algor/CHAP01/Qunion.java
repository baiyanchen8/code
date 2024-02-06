
public class Qunion {
    
    private  int [] id;
    //

    public Qunion (int n){
        int i;
        id =new int[n];
        for(i=0;i<n;i++){
            id [i]=i;

        }
    }
    public static void main(String[] args) {
        Qunion nQunion=new Qunion(4);
        nQunion.union(1, 2);
        nQunion.union(2, 3);
        nQunion.union(3, 1);
        for(int i=0;i<4;i++){
              System.out.println(i+"  "+nQunion.find1(i)+"  "+nQunion.find(i));
        }
      
    }
    public int find(int p){
        while(p!=id[p]) p=id[p];
        return p;
    }
    public int find1(int p){
        p=id[p];
        return p;
    }
    public void union (int p,int q){
        int pid =find(p);
        int qid =find(q);
        id[pid]=qid;
    }
}
