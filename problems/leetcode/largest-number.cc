// https://leetcode.com/problems/largest-number/
/*
Brute Force:
============
1. Convert all to string.
2. Inverse sort array based on digit order.
3. return "".join(nums)

TC: O(N log N)
SC: O(N), where N = len(nums).
*/

class Solution {
public:
    string largestNumber(vector<int>& nums) {
        vector<std::string> stringNums;
        for (const auto num : nums) {
            stringNums.push_back(std::to_string(num));
        }

        std::sort(stringNums.begin(), stringNums.end(),
            [](const std::string& a, const std::string& b) {
                return a + b > b + a; });

        if (stringNums[0] == "0") {
            return "0";
        }

        std::string largest;
        for (const auto& num : stringNums) {
            largest += num;
        }

        return largest;
    }
};
