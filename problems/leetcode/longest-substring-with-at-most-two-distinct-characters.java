// https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
      int start = 0, end = 0, maxLength = 0;
      int[] map = new int[128];
      int counter = 0;
      
      while (end < s.length()) {
        if (map[s.charAt(end)] == 0) {
          counter++;
        }

        map[s.charAt(end)]++;
        
        if (counter <= 2) {
          maxLength = Math.max(maxLength, end - start + 1);
        }
        
        while (counter > 2) {
          map[s.charAt(start)]--;
          if (map[s.charAt(start)] == 0) {
            counter--;
          }

          start++;
        }
        
        end++;
      }
      
      return maxLength;
    }
}
