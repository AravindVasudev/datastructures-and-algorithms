class Solution {
    public void rotate(int[][] matrix) {
        int N = matrix.length;

        // transpose
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        // reverse every row
        for (int i = 0; i < N; i++) {
            int j = 0, k = N - 1;
            while (j < k) {
                int temp = matrix[i][j];
                matrix[i][j++] = matrix[i][k];
                matrix[i][k--] = temp;
            }
        }

    }
}
