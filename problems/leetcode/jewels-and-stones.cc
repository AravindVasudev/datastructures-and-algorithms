// https://leetcode.com/problems/jewels-and-stones/
class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        unordered_map<char, int> stoneCount;
        for (char c : stones) {
            stoneCount[c]++;
        }

        int result = 0;
        for (char jewel : jewels) {
            result += stoneCount[jewel];
        }

        return result;
    }
};
