import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MatrixSpiralTraversal {

    private static List<Integer> spiralTraversal(int[][] matrix, int layer, int depth) {
        int M = matrix.length;
        int N = matrix[0].length;
        List<Integer> traversal = new ArrayList<>(M * N);

        if (depth <= 0) {
            return null;
        }

        /**
         * Peeling the outer layer
         */
            for (int j = layer; j < N - layer; j++) { // first row
            traversal.add(matrix[layer][j]);
        }

        for (int i = layer + 1; i < M - layer; i++) { // last col
            traversal.add(matrix[i][N - 1 - layer]);
        }

        for (int j = N - 2 - layer; j >= layer; j--) { // last row
            traversal.add(matrix[M - 1 - layer][j]);
        }

        for (int i = M - 2 - layer; i>= layer + 1; i--) { // first col
            traversal.add(matrix[i][layer]);
        }

        if (depth > 1) {
            List<Integer> subMatrix = spiralTraversal(matrix, layer + 1, depth - 1);
            if (subMatrix != null) {
                traversal.addAll(subMatrix);
            }
        }

        return traversal;
    }

    private static int iLog2(int n) {
        return (int) Math.ceil(Math.log(n) / Math.log(2));
    }

    private static List<Integer> spiralTraversal(int[][] matrix) {
        int depth = Math.min(iLog2(matrix.length), iLog2(matrix[0].length));
        return spiralTraversal(matrix, 0, depth);
    }

    public static void main(String[] args) {
        int M = 5;
        int N = 4;
        int[][] matrix = new int[M][N];

        // Fill the matrix
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                matrix[i][j] = (i * N) + j + 1;
            }
        }

        // Input Matrix
        System.out.println(Arrays.deepToString(matrix));

        System.out.println(spiralTraversal(matrix));


        int[][] m2 = new int[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                m2[i][j] = (i * 3) + j + 1;
            }
        }

        System.out.println(Arrays.deepToString(m2));
        System.out.println(spiralTraversal(m2));
    }
}
