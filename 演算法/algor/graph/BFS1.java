import java.util.*;

public class BFS1 {
    public void bfs(int[][] edges, int startVertex) {
        Set<Integer> visited = new HashSet<>();
        Queue<Integer> queue = new LinkedList<>();

        queue.add(startVertex);
        visited.add(startVertex);

        while (!queue.isEmpty()) {
            int currentVertex = queue.poll();
            System.out.println(currentVertex); // Process or visit the current vertex

            // Enqueue all unvisited neighboring vertices
            for (int[] edge : edges) {
                int from = edge[0];
                int to = edge[1];
                if (from == currentVertex && !visited.contains(to)) {
                    queue.add(to);
                    visited.add(to);
                }
            }
        }
    }

    // Example usage
    public static void main(String[] args) {
        int[][] edges = {
            {1, 2},
            {1, 3},
            {2, 4},
            {2, 5},
            {3, 5},
            {4, 6}
        };

        BFS1 bfs = new BFS1();
        bfs.bfs(edges, 1);
    }
}
