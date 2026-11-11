import java.util.*;

public class GraphTraversal {

    private Map<Character, List<Character>> graph =
            new LinkedHashMap<>();

    // Add vertex
    void addVertex(char vertex) {
        graph.putIfAbsent(vertex, new ArrayList<>());
    }

    // Add undirected edge
    void addEdge(char first, char second) {

        addVertex(first);
        addVertex(second);

        graph.get(first).add(second);
        graph.get(second).add(first);
    }

    // BFS - Breadth First Search
    void BFS(char start) {

        Set<Character> visited = new LinkedHashSet<>();
        Queue<Character> queue = new LinkedList<>();

        visited.add(start);
        queue.add(start);

        System.out.print("BFS: ");

        while (!queue.isEmpty()) {

            char current = queue.remove();

            System.out.print(current + " ");

            for (char neighbor : graph.get(current)) {

                if (!visited.contains(neighbor)) {

                    visited.add(neighbor);
                    queue.add(neighbor);
                }
            }
        }

        System.out.println();
    }

    // DFS - Depth First Search
    void DFS(char vertex, Set<Character> visited) {

        visited.add(vertex);

        System.out.print(vertex + " ");

        for (char neighbor : graph.get(vertex)) {

            if (!visited.contains(neighbor)) {

                DFS(neighbor, visited);
            }
        }
    }

    public static void main(String[] args) {

        GraphTraversal g = new GraphTraversal();

        // Graph connections for BAJENTING

        g.addEdge('B', 'A');
        g.addEdge('B', 'J');

        g.addEdge('A', 'E');
        g.addEdge('A', 'N');

        g.addEdge('J', 'T');
        g.addEdge('J', 'I');

        g.addEdge('E', 'G');
        g.addEdge('N', 'G');

        g.addEdge('G', 'T');

        System.out.println("================================");
        System.out.println(" GRAPH - BAJENTING");
        System.out.println("================================");

        System.out.println("\nGraph Connections:");

        for (char vertex : g.graph.keySet()) {
            System.out.println(vertex + " -> " + g.graph.get(vertex));
        }

        System.out.println("\nTraversal Results:");

        g.BFS('B');

        System.out.print("DFS: ");

        Set<Character> visited = new LinkedHashSet<>();

        g.DFS('B', visited);

        System.out.println();
    }
}
