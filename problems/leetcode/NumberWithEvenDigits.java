// https://leetcode.com/problems/find-numbers-with-even-number-of-digits
class Solution {
    public int findNumbers(int[] nums) {
        int count = 0;
        for (int num : nums) {
            count += (Integer.toString(num).length() % 2 == 0) ? 1 : 0;
        }

        return count;
    }
}
