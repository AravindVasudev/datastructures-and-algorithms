// https://leetcode.com/problems/find-the-original-typed-string-i/
class Solution {
public:
    int possibleStringCount(string word) {
        int combinations = 1;
        
        const int N = word.size();
        for (int i = 1; i < N; i++) {
            int length = 1;
            while (i < N && word[i] == word[i - 1]) {
                length++;
                i++;
            }

            combinations += length - 1;
        }

        return combinations;
    }
};
