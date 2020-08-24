// https://leetcode.com/problems/triangle/
class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        // memo[][] - 
        // fn(triangle, row, col, memo) -> min path value for row, col
        
        if (triangle == null || triangle.size() == 0) {
            return 0;
        }
        
        int M = triangle.size();
        int N = triangle.get(M - 1).size();
        
        int[][] memo = new int[M][N];
        for (int i = 0; i < N; i++) {
            memo[M - 1][i] = triangle.get(M - 1).get(i);
        }
        
        for (int i = M - 2; i >= 0; i--) {
            N = triangle.get(i).size();
            for (int j = 0; j < N; j++) {
                memo[i][j] = Math.min(memo[i + 1][j], memo[i + 1][j + 1]) + triangle.get(i).get(j);
            }
        }
        
        return memo[0][0];
    }
}
