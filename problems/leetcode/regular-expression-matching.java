# https://leetcode.com/problems/regular-expression-matching/
# Top Down Approach
class Solution {
  public boolean isMatch(String s, String p) {
    Boolean[][] memo = new Boolean[s.length() + 1][p.length() + 1];
    return isMatch(s, p, 0, 0, memo);
  }
  
  private boolean isMatch(String text, String pattern, int textIndex, int patternIndex, Boolean[][] memo) {
    if (memo[textIndex][patternIndex] != null) {
      return memo[textIndex][patternIndex];
    }
    
    boolean result;
    if (patternIndex == pattern.length()) {
      result = textIndex == text.length();
    } else {
      boolean firstMatch = (textIndex < text.length() &&
                            (pattern.charAt(patternIndex) == text.charAt(textIndex) ||
                            pattern.charAt(patternIndex) == '.'));
      
      if (patternIndex + 1 < pattern.length() && pattern.charAt(patternIndex + 1) == '*') {
        result = isMatch(text, pattern, textIndex, patternIndex + 2, memo) ||
          (firstMatch && isMatch(text, pattern, textIndex + 1, patternIndex, memo));
      } else {
        result = firstMatch && isMatch(text, pattern, textIndex + 1, patternIndex + 1, memo);
      }
    }
    
    memo[textIndex][patternIndex] = result;
    return result;
  }
}

# Bottom Up Approach
# TODO
