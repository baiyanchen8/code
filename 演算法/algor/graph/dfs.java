class dfs{
    int [][] arr;
    boolean [] visit;
    int [] prepoiont;
    int now;
    int topologic[];
    public static void main(String[] args) {
        dfs tDfs =new dfs();
        
        tDfs.dfs1(5);
        for(int i=0;i<5;i++){
            if(arr)
        }
        for (int ak : tDfs.topologic) {
            System.out.print(ak+"   ");
        }
    }
    public dfs(){
        topologic=new int[6];
        now=1;
        arr=new int[5][2];
        arr[0][0]=1;arr[0][1]=2;//1->2
        arr[1][0]=2;arr[1][1]=3;//2->3
        arr[2][0]=3;arr[2][1]=4;//3->4
        arr[3][0]=1;arr[3][1]=5;//1->5
        arr[4][0]=5;arr[4][1]=4;//5->7
        visit=new boolean[6];
        prepoiont=new int[6]; 
    }
    public void dfs1(int start){
        visit[start]=true;
        for (int[] is : arr) {
            // if(is[1]==start){
            //     int next=is[0];
            //     if(visit[next]==false){
            //         prepoiont[next]=start;
            //         visit[next]=true;
            //         System.out.println(start+"==>"+next);
            //         dfs1(next);
            //     }
            // }
            if(is[0]==start){
                int next=is[1];
                if(visit[next]==false){
                    prepoiont[next]=start;
                    visit[next]=true;
                    System.out.println(start+"==>"+next);
                    dfs1(next);
                }
            }
        }
        topologic[now-1]=start;
        now++;
    }
}