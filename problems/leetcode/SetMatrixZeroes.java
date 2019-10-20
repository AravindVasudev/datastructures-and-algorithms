class Solution {
    public void setZeroes(int[][] matrix) {
      int M = matrix.length;
      int N = matrix[0].length;

      Set<Integer> rows = new HashSet<>(M);
      Set<Integer> cols = new HashSet<>(N);

      for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
          if (matrix[i][j] == 0) {
            rows.add(i);
            cols.add(j);
          }
        }
      }

      for (Integer i : rows) {
        for (int j = 0; j < N; j++) {
          matrix[i][j] = 0;
        }
      }

      for (Integer j : cols) {
        for (int i = 0; i < M; i++) {
          matrix[i][j] = 0;
        }
      }

    }
}
