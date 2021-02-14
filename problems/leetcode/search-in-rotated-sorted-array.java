// https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution {
    public int search(int[] nums, int target) {
        // Find the pivot
        int left = 0, right = nums.length - 1;
        
        while (left < right) {
            int mid = (left + right) / 2;
            
            if (nums[mid] < nums[right]) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        
        int pivot = left;
        left = 0;
        right = nums.length - 1;
        
        // Check which half of the array does the target lie
        if (target >= nums[pivot] && target <= nums[right]) {
            left = pivot;
        } else {
            right = pivot - 1;
        }
        
        // Search in that half
        while (left <= right) {
            int mid = (left + right) / 2;
            
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return -1;
    }
}
