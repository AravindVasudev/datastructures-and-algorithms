// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
class Solution {
    public int findMin(int[] nums) {
        if (nums.length == 0) return 0;

        int prev = Integer.MIN_VALUE;
        boolean found = false;
        for (int num : nums) {
            if (prev > num) {
                found = true;
                prev = num;
                break;
            }

            prev = num;
        }

        return found ? prev : nums[0];
    }
}
