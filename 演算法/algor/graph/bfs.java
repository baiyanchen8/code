import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;

class bfs{
    public static void main(String[] args) {
        int [][]edge ={
            {1,2},
            {2,3},
            {1,5},
            {2,4},
            {3,4}
        };
        bfs tbfs=new bfs(edge,1);
    }
    public bfs(int [][] edge,int start){
        Set<Integer> visit=new HashSet<>();
        Queue<Integer> aQueue =new LinkedList<>();
        aQueue.add(start);
        visit.add(start);
        while(!aQueue.isEmpty()){
            int now=aQueue.poll();
            System.out.println(now);
            for (int[] is : edge) {
                if(is[0]==now){
                    int next= is[1];
                    if(!visit.contains(next)){
                        aQueue.add(next);
                        visit.add(next);
                    }
                }
                if(is[1]==now){
                    int next= is[0];
                    if(!visit.contains(next)){
                        aQueue.add(next);
                        visit.add(next);
                    }
                }
            }
        }

    }

}