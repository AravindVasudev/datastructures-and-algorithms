// https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution {
    public int lengthOfLongestSubstring(String s) {
      int[] seen = new int[128];
      int maxLength = 0;
      
      for (int start = 0, end = 0; end < s.length(); end++) {
        start = Math.max(seen[s.charAt(end)], start);
        maxLength = Math.max(maxLength, end - start + 1);
        seen[s.charAt(end)] = end + 1;
      }

      return maxLength;
    }
}
