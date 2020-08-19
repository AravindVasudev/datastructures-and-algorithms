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
// TBD
