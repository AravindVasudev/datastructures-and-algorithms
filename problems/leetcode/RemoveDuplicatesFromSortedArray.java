class Solution {
    public int removeDuplicates(int[] nums) {
        int newIndex = 1;

        for (int i = 0 ; i < nums.length;) {
            int j = i + 1;
            while (j < nums.length && nums[i] == nums[j]) j++;
            if (j == nums.length) break;

            nums[newIndex++] = nums[j];
            i = j;
        }

        return newIndex;
    }
}
