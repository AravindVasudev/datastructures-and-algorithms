// https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
class Solution {
    public int solution(int N) {
        int maxGap = 0;
        
        while (N > 0) {
            int lastBit = N & 1;
            N >>= 1;
            
            if (lastBit == 1) {
                int currentGap = 0;
                while (N > 0 && (N & 1) != 1) {
                    currentGap += 1;
                    N >>= 1;
                }
                
                if ((N & 1) == 1) {
                    maxGap = Math.max(maxGap, currentGap);
                }
            }
        }
        
        return maxGap;
    }
}
