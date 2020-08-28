// https://leetcode.com/problems/wildcard-matching/
class Solution {
    public boolean isMatch(String s, String p) {
        Boolean[][] memo = new Boolean[s.length()][p.length()];
        return isMatch(s, p, 0, 0, memo);
    }
    
    private boolean isMatch(String s, String p, int sIndex, int pIndex, Boolean[][] memo) {
        if (sIndex == s.length()) {
            while (pIndex < p.length() && p.charAt(pIndex) == '*') {
                pIndex++;
            }
            
            return pIndex == p.length();
        }
        
        if (pIndex == p.length()) {
            return false;
        }
        
        if (memo[sIndex][pIndex] != null) {
            return memo[sIndex][pIndex];
        }
        
        char currentStringChar = s.charAt(sIndex);
        char currentPatternChar = p.charAt(pIndex);

        if (currentPatternChar != '*') {
            return memo[sIndex][pIndex] = (currentPatternChar == '?' ||
                                           currentPatternChar == currentStringChar) &&
                                            isMatch(s, p, sIndex + 1, pIndex + 1, memo);
        }
        
        return memo[sIndex][pIndex] = isMatch(s, p, sIndex + 1, pIndex, memo) ||
            isMatch(s, p, sIndex, pIndex + 1, memo);
    }
}
