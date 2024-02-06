
public class WunionPC {
    
    private int [] id;
    private int [] si;

    public WunionPC (int n){
        int i;
        id =new int[n];
        si =new int[n];
        for(i=0;i<n;i++){
            id [i]=i;
            si[i]=1;
        }
    }
    public static void main(String[] args) {
        WunionPC nWunion=new WunionPC(10);
       
        nWunion.union(3, 2);
        nWunion.union(3, 4);
        nWunion.union(5, 4);
        nWunion.union(5, 6);
        for(int i=0;i<10;i++){
              System.out.println(i+"->"+nWunion.id[i]+" "+nWunion.find(i));
        }
        nWunion.connected(1, 2);
    }
    public int find(int p){
        while(p!=id[p]) {
            id[p]=id[id[p]];
            p=id[p];
        }
        
        return p;
    }
    public void  connected(int p,int q){
        if(find(p)==find(q)){
            System.out.println(p+" is connected to "+q);
        }else{
            System.out.println(p+" isn't connected to "+q);
        }
        
    }
    public void union (int p,int q){
        int pid =find(p);
        int qid =find(q);
        if(si[pid]>si[qid]){
            id[pid]=qid;
            si[qid]+=si[pid];
        }else{
            id[qid]=pid;
            si[pid]+=si[qid];
        }
    }
}
