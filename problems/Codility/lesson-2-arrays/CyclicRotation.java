class Solution {
    private void reverseRange(int[] A, int i, int j) {
        while (i < j) {
            int temp = A[i];
            A[i] = A[j];
            A[j] = temp;
            
            i++;
            j--;
        }
    }
    
    public int[] solution(int[] A, int K) {
        if (A == null || A.length == 0) {
            return A;
        }

        K %= A.length;

        reverseRange(A, 0, A.length - 1);
        reverseRange(A, 0, K - 1);
        reverseRange(A, K, A.length - 1);
        
        return A;
    }
}
