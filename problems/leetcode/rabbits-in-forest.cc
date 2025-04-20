// https://leetcode.com/problems/rabbits-in-forest/
/**
 * Breakdown:
 * ==========
 * Rabbits #: Unknown
 * Given: answers, where ans is ith rabbit ans to how many with similar color.
 * Ret: min(rabbits).
 *
 * ans = [1, 1, 2]
 * 1: 2, 2: 1 -> 1: 1, 2: 1 -> 5
 * 10: 1 -> 10: 3 -> 11
 * 
 * 1: 5
 * Brute Force:
 * ============
 * 1. Convert to map[ans] -> count. O(N)
 * 2. Foreach ans, dedup and add to res.
 *  2.1. count / (ans + 1).
 * 3. ret result.
 */

class Solution {
public:
    int numRabbits(vector<int>& answers) {
        // 1. Convert to map[ans] -> count.
        std::unordered_map<int, int> count;
        for (const int answer : answers) {
            count[answer]++;
        }

        // 2. foreach ans, dedup & add to res.
        int res{};
        for (const auto& c : count) {
            res += static_cast<int>(ceil((double)c.second / (c.first + 1))) * (c.first + 1);
        }

        // 3. Ret result
        return res;
    }
};
