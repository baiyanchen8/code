public class linklist{
    private class node{
        
        int item ;
        node next;
        public node(int a){
            item=a;
            next=null;
        }
    }
    node head=new node(0);
    public void push(int i)
    {   
        if(head.next==null){
            head.next=new node(i);
            
            return;
        }
        node now=head;    
        while(now.next!=null){
            now=now.next;
        }
        now.next=new node(i);
        now.next.next=null;
    }
    public int pop()
    {   
        if(head==null){
            return -1;
        }
        node now=head.next;    
        node past=head;
        while(now!=null&&now.next!=null){
            past=past.next;
            now=now.next;
        }
        int i=0;
        if(now!=null){
            i =now.item;
            past.next=null;
        }else{
            i=past.item;
            past=null;
        }
        return i;
        
    }
    public static void main(String[] args) {
        linklist a= new linklist();
        int n=10;
        for(int i=0;i<n;i++){
            a.push(i);
        }
        for(int i=0;i<n;i++){
            System.out.print(" "+a.pop());
        }
    }
}