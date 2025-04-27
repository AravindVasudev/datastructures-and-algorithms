// https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition
class Solution {
public:
    int countSubarrays(vector<int>& nums) {
        const int N = nums.size();
        int count{};

        for (int i = 0; i < N - 2; i++) {
            if (nums[i + 1] == (nums[i] + nums[i + 2]) * 2) {
                count++;
            }
        }

        return count;
    }
};
