// https://leetcode.com/problems/concatenation-of-array/
impl Solution {
    pub fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
        let mut nums2 = nums.clone();
        nums2.extend(nums);

        nums2
    }
}
