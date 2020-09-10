// https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
      int[] map = new int[128];
      int maxLength = 0;
      int distinctCounter = 0;
      
      for (int start = 0, end = 0; end < s.length(); end++) {
        if (map[s.charAt(end)] == 0) {
          distinctCounter++;
        }
        
        map[s.charAt(end)]++;
        
        if (distinctCounter <= k) {
          maxLength = Math.max(maxLength, end - start + 1);
        }
        
        while (distinctCounter > k) {
          map[s.charAt(start)]--;
          if (map[s.charAt(start)] == 0) {
            distinctCounter--;
          }
          
          start++;
        }
      }
      
      return maxLength;
    }
}
