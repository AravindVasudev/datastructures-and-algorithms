class Solution {
    public int coinChange(int[] coins, int amount) {       
        int[] memo = new int[amount + 1];
        Arrays.fill(memo, -1);
        
        memo[0] = 0;
        for (int i = 1; i <= amount; i++) {
            for (int c = 0; c < coins.length; c++) {
                if (i >= coins[c]) {
                    int curWays = memo[i - coins[c]];
                    
                    if (curWays != -1) {
                        memo[i] = memo[i] != -1 ? Math.min(memo[i], curWays + 1) : curWays + 1;
                    }
                }
            }
        }
        
        return memo[amount];
    }
}