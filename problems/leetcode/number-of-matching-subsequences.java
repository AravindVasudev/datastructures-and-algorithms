// https://leetcode.com/problems/number-of-matching-subsequences/
import java.text.StringCharacterIterator;

class Solution {
    public int numMatchingSubseq(String S, String[] words) {
        int count = 0;
        List<StringCharacterIterator>[] heads = new List[26];
        
        for (int i = 0; i < 26; i++) {
            heads[i] = new ArrayList<StringCharacterIterator>();
        }
        
        for (String word : words) {
            heads[word.charAt(0) - 'a'].add(new StringCharacterIterator(word));
        }
        
        for (char c : S.toCharArray()) {
            List<StringCharacterIterator> previous = heads[c - 'a'];
            heads[c - 'a'] = new ArrayList<StringCharacterIterator>();
            
            for (StringCharacterIterator it : previous) {
                char next = it.next();
                if (next == it.DONE) {
                    count++;
                    continue;
                }
                
                heads[next - 'a'].add(it);
            }
        }
        
        return count;
    }
}
