// https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
class Solution {
    public boolean search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        
        while (left <= right) {
            int mid = (left + right) / 2;
            
            if (target == nums[mid]) {
                return true;
            }
            
            // Right is sorted or left is unsorted
            if (nums[mid] < nums[right] || nums[mid] < nums[left]) {
                if (target > nums[mid] && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            } else if (nums[left] < nums[mid] || nums[right] < nums[mid]) {
                if (target >= nums[left] && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                right--;
            }
        }
        
        return false;
    }
}
