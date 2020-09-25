// https://leetcode.com/problems/koko-eating-bananas/
class Solution {
    public int minEatingSpeed(int[] piles, int H) {
        if (piles.length == 0) {
            return 0;
        }

        int low = 1;
        int high = 1;
        for (int pile : piles) {
            high = Math.max(high, pile);
        }
        
        while (low < high) {
            int mid = (low + high) / 2;
            
            if (canKokoFinish(piles, H, mid)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        
        return low;
    }
    
    private boolean canKokoFinish(int[] piles, int H, double K) {
        int hours = 0;
        
        for (int pile : piles) {
            hours += (int) Math.ceil(pile / K);
        }
        
        return hours <= H;
    }
}
