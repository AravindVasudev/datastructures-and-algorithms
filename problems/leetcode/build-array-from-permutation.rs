// https://leetcode.com/problems/build-array-from-permutation/
impl Solution {
    pub fn build_array(nums: Vec<i32>) -> Vec<i32> {
        let mut ans = vec![0; nums.len()];
        for (idx, num) in nums.iter().enumerate() {
            ans[idx] = nums[*num as usize];
        }

        ans
    }
}
