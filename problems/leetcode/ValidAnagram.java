class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
          return false;
        }

      char[] sArr = s.toCharArray();
      char[] tArr = t.toCharArray();

      Arrays.sort(tArr);
      Arrays.sort(sArr);

      for (int i = 0; i < sArr.length; i++) {
        if (sArr[i] != tArr[i]) {
          return false;
        }
      }

      return true;
    }
}
