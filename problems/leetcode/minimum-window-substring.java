// https://leetcode.com/problems/minimum-window-substring/
class Solution {
    public String minWindow(String s, String t) {
      int[] tMap = new int[128];
      
      for (char c : t.toCharArray()) {
        tMap[c]++;
      }
      
      int start = 0, end = 0, counter = t.length(), minStart = -1, minLen = Integer.MAX_VALUE;
      
      while (end < s.length()) {
        if (tMap[s.charAt(end)] > 0) {
          counter--;
        }
        
        tMap[s.charAt(end)]--;
        end++;
        
        while (counter == 0) {
          if (minLen > end - start) {
            minLen = end - start;
            minStart = start;
          }
          
          tMap[s.charAt(start)]++;
          if (tMap[s.charAt(start)] > 0) {
            counter++;
          }

          start++;          
        }
      }
      
      return minStart == -1 ? "" : s.substring(minStart, minStart + minLen);
    }
}
