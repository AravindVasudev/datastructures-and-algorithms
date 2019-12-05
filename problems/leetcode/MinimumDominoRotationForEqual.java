class Solution {
    public int minDominoRotations(int[] A, int[] B) {
        int[] aCount = new int[6], bCount = new int[6];
        for (int i = 0; i < A.length; i++) {
            aCount[A[i] - 1]++;
            bCount[B[i] - 1]++;
        }
        
        int aMax = -1, bMax = -1;
        int aMaxCount = -1, bMaxCount = -1;
        for (int i = 0; i < 6; i++) {
            if (aMaxCount < aCount[i]) {
                aMaxCount = aCount[i];
                aMax = i + 1;
            }
            
            if (bMaxCount < bCount[i]) {
                bMaxCount = bCount[i];
                bMax = i + 1;
            }
        }
        
        // Solved case
        if (aMaxCount == A.length || bMaxCount == A.length) {
            return 0;
        }
        
        boolean aPossible = true, bPossible = true;
        int aSwaps = 0, bSwaps = 0;
        for (int i = 0; i < A.length && (aPossible || bPossible); i++) {
            if (aPossible && (A[i] != aMax)) {
                if (B[i] == aMax) {
                    aSwaps++;   
                } else {
                    aPossible = false;
                    aSwaps = 0;
                }
            }
            
            if (bPossible && (B[i] != bMax)) {
                if (A[i] == bMax) {
                    bSwaps++;
                } else {
                    bPossible = false;
                    bSwaps = 0;
                }
            }
        }
        
        if (aSwaps != 0 && bSwaps != 0) {
            return Math.min(aSwaps, bSwaps);
        } else if (aSwaps == 0 && bSwaps == 0) {
            return -1; // No solution
        } else {
            return Math.max(aSwaps, bSwaps); // One face has no solution
        }
            
    }
}