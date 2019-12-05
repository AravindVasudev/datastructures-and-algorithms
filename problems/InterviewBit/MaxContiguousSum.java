public class Solution {
    // DO NOT MODIFY THE LIST. IT IS READ ONLY
    public int maxSubArray(final List<Integer> A) {
        int windowSum = 0, maxSum = 0, smallest = Integer.MIN_VALUE;
        int N = A.size();
        for (int i = 0; i < N; i++) {
            windowSum += A.get(i);
            if (windowSum < 0) {
                windowSum = 0;
            }
            
            if (maxSum < windowSum) {
                maxSum = windowSum;
            }
            
            if (smallest < A.get(i)) {
                smallest = A.get(i);
            }
        }
        
        return maxSum == 0 ? smallest : maxSum;
    }
}
