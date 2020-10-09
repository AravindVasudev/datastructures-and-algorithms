// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution {
    public int[] searchRange(int[] nums, int target) {
      if (nums.length == 0) {
        return new int[] {-1, -1};
      }
      
      int lo = 0, hi = nums.length - 1;
      
      while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        
        if (nums[mid] == target) {
          hi = mid;
        } else if (nums[mid] < target) {
          lo = mid + 1;
        } else {
          hi = mid - 1;
        }
      }
      
      if (nums[lo] != target) {
        return new int[] {-1, -1};
      }
      
      int begining = lo;
      hi = nums.length - 1;
      
      while (lo < hi) {
        int mid = lo + (hi - lo + 1) / 2;
        
        if (nums[mid] == target) {
          lo = mid;
        } else if (nums[mid] < target) {
          lo = mid + 1;
        } else {
          hi = mid - 1;
        }
      }
      
      return new int[] {begining, lo};
    }
}
