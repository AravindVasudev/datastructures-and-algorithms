# https://leetcode.com/problems/word-break/
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        return wordBreak(s, new HashSet(wordDict), 0, new Boolean[s.length()]);
    }
    
    private boolean wordBreak(String s, Set<String> wordDict, int startIndex, Boolean[] memo) {
        if (startIndex == s.length()) {
            return true;
        }
        
        if (memo[startIndex] != null) {
            return memo[startIndex];
        }
        
        for (int endIndex = startIndex + 1; endIndex <= s.length(); endIndex++) {
            if (wordDict.contains(s.substring(startIndex, endIndex)) && wordBreak(s, wordDict, endIndex, memo)) {
                return memo[startIndex] = true;
            }
        }
        
        return memo[startIndex] = false;
    }
}

// Bottom Up
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> wordDictSet = new HashSet(wordDict);
        boolean[] dp = new boolean[s.length() + 1];
        
        dp[0] = true;
        for (int i = 1; i <= s.length(); i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && wordDictSet.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        
        return dp[s.length()];
    }
}
