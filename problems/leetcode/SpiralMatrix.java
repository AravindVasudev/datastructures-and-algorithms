// https://leetcode.com/problems/spiral-matrix
class Solution {
    private List<Integer> spiralOrder(int[][] matrix, int layer) {
        int M = matrix.length - layer; // rows
        int N = matrix[0].length - layer; // cols
        
        List<Integer> traversal = new ArrayList<>();
        
        // Base Case
        if ((layer >= M) || (layer >= N)) {
            return traversal;
        }
        
        // Peeling the outer layer       
        for (int j = layer; j < N; j++) { // first row
            traversal.add(matrix[layer][j]);
        }
        
        for (int i = layer + 1; i < M; i++) { // last col
            traversal.add(matrix[i][N - 1]);
        }
        
        if ((layer < M - 1) && (layer < N - 1)) {
            for (int j = N - 2; j >= layer; j--) { // last row
                traversal.add(matrix[M - 1][j]);
            }
        
            for (int i = M - 2; i > layer; i--) { // first col
                traversal.add(matrix[i][layer]);
            }
        }
        
        traversal.addAll(spiralOrder(matrix, layer + 1));
        return traversal;
    }
    
    public List < Integer > spiralOrder(int[][] matrix) {
        if (matrix == null || matrix.length == 0) {
            return new ArrayList<Integer>();
        }
        
        return spiralOrder(matrix, 0);
    }
}