// https://leetcode.com/problems/friend-circles/
class Solution {
    public int findCircleNum(int[][] M) {
        if (M == null || M.length == 0) {
            return 0;
        }
        
        int circles = 0;
        for (int student = 0; student < M.length; student++) {
            if (M[student][student] == 1) {
                dfs(M, student);
                circles++;
            }
        }
        
        return circles;
    }
    
    private void dfs(int[][] M, int student) {
        if (M[student][student] == 0) {
            return;
        }
        
        M[student][student] = 0;
        for (int connection = 0; connection < M.length; connection++) {
            if (M[student][connection] == 1) {
                dfs(M, connection);
            }
        }
    }
}
