public class Solution {
    public int coverPoints(ArrayList<Integer> A, ArrayList<Integer> B) {
        if (A.size() == 0 || A.size() == 1) return 0;
        
        int steps = 0, N = A.size();
        for (int i = 0; i < N - 1; i++) {
            steps += distance(A.get(i), B.get(i), A.get(i + 1), B.get(i + 1));
        }
        
        return steps;
    }
    
    private int distance(int x1, int y1, int x2, int y2) {
        return Math.max(Math.abs(x1 - x2), Math.abs(y1 - y2));
    }
}
