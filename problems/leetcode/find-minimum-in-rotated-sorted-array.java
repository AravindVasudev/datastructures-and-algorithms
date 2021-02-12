// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution {
    public int findMin(int[] nums) {
        int left = 0, right = nums.length - 1;
        int rightVal = nums[right];
        
        while (left < right) {
            int mid = (left + right) / 2;
            if (nums[mid] < rightVal) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        
        return nums[left];
    }
}
