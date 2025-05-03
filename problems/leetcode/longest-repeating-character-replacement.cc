// https://leetcode.com/problems/longest-repeating-character-replacement/
class Solution {
public:
    int characterReplacement(string s, int k) {
        int start{}, longest{}, max{};
        std::unordered_map<char, int> window;

        for (int end = 0; end < s.size(); end++) {
            window[s[end]]++; // add end to window.
            max = std::max(max, window[s[end]]);

            if (end - start + 1 - max > k) {
                window[s[start++]]--; // remove start from window.
            }

            longest = std::max(longest, end - start + 1);
        }

        return longest;
    }
};
