int bfsComponentSize(boolean[][] matrix) {
    int size = 1;
    
    Queue<Integer> q = new LinkedList<>();
    Set<Integer> visited = new HashSet<>();
    q.add(1);
    visited.add(1);
    
    while (!q.isEmpty()) {
        int curNode = q.poll();
        
        for (int j = 0; j < matrix.length; j++) {
            if (matrix[j][curNode] && !visited.contains(j)) {
                size++;
                q.add(j);
                visited.add(j);
            }
        }
    }
    
    return size;
}
