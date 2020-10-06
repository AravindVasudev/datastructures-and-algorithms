//https://leetcode.com/problems/valid-parenthesis-string/
class Solution {
    public boolean checkValidString(String s) {
      Boolean[][] memo = new Boolean[s.length()][s.length()];
      
      return checkValidString(s, 0, 0, memo);
    }
  
    private boolean checkValidString(String s, int index, int open, Boolean[][] memo) {
      if (index == s.length()) {
        return open == 0;
      }
      
      if (open < 0) {
        return false;
      }
      
      if (memo[index][open] != null) {
        return memo[index][open];
      }
      
      switch (s.charAt(index)) {
        case '(':
          memo[index][open] = checkValidString(s, index + 1, open + 1, memo);
          break;
        case ')':
          memo[index][open] = checkValidString(s, index + 1, open - 1, memo);
          break;
        default:
          memo[index][open] = checkValidString(s, index + 1, open + 1, memo) ||
            checkValidString(s, index + 1, open - 1, memo) ||
            checkValidString(s, index + 1, open, memo);
      }
      
      return memo[index][open];
    }
}
