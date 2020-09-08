// https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
class Solution {
    public String findLongestWord(String s, List<String> d) {
        String maxString = "";
        for (String str : d) {
            if (isSubsequence(s, str)) {
                if (str.length() > maxString.length() ||
                    (str.length() == maxString.length() && str.compareTo(maxString) < 0)) {
                    maxString = str;
                }
            }
        }
        
        return maxString;
    }
    
    public boolean isSubsequence(String x, String y) {
        int j = 0;       
        for (int i = 0; i < x.length() && j < y.length(); i++) {
            if (x.charAt(i) == y.charAt(j)) {
                j++;
            }
        }
        
        return j == y.length();
    }
}
