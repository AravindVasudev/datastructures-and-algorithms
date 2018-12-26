class Solution {
    public int lengthOfLongestSubstring(String s) {
        int longest = 0;
        for (int i = 0; i < s.length(); i++) {
            HashSet<Character> seen = new HashSet<>();
            int cur = 0;
            for (int j = i; j < s.length(); j++) {
                if (seen.contains(s.charAt(j))) break;
                seen.add(s.charAt(j));
                cur++;
            }
            
            longest = longest > cur ? longest : cur;
        }
        
        return longest;
    }
}
