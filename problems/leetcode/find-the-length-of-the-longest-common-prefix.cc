// https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/
class Solution {
public:
    int longestCommonPrefix(vector<int>& arr1, vector<int>& arr2) {
        unordered_set<int> prefixes;
        for (int num : arr1) {
            while (!prefixes.contains(num) && num > 0) {
                prefixes.insert(num);
                num /= 10;
            }
        }

        int longest = 0;
        for (int num : arr2) {
            while (!prefixes.contains(num) && num > 0) {
                num /= 10;
            }

            if (num > 0) {
                longest = std::max(longest, static_cast<int>(log10(num)) + 1);
            }
        }

        return longest;
    }
};
