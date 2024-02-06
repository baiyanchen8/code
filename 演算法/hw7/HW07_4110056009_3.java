public class HW07_4110056009_3{
    public boolean checkLLK(int[][] points){
        for(int[] mid : points){
            HashSet set = new HashSet();
            for(int[] point : points){
                if(mid[0] == point[0] && mid[1] == point[1]){
                    continue;
                }
                final double slope = (mid[0] == point[0] ? 1e9 : (point[1] - mid[1]) / (double)(point[0] - mid[0]));
                if(set.contains(slope)){
                    return true;
                }
                set.add(slope);
            }
        }
        return false;
    }
}

class HashSet{
    private static final int CAPACITY = 1 << 16;
    private Node[] table = new Node[CAPACITY];

    static class Node{
        final double key;
        Node next;
        
        Node(double key, Node next){
            this.key = key;
            this.next = next;
        }
    }

    public HashSet() {
    }

    static final int hash(double key) {
        int h = Double.hashCode(key);
        return ((h ^ (h >>> 16)) & (CAPACITY - 1));
    }

    public void add(double key){
        final int h = hash(key);
        Node newNode = new Node(key, table[h]);
        table[h] = newNode;
    }

    public void remove(double key){
        final int h = hash(key);
        Node node = table[h];
        if(node == null) return;
        if(node.key == key) table[h] = node.next;
        else{
            while(node != null && node.next != null){
                if(node.next.key == key){
                    node.next = node.next.next;
                    return;
                }
                node = node.next;
            }
        }
    }

    public boolean contains(double key){
        final int h = hash(key);
        Node node = table[h];
        while(node != null){
            if(node.key == key){
                return true;
            }
            node = node.next;
        }
        return false;
    }
}