class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
      List<List<Integer>> solution = new ArrayList<>();
      Arrays.sort(nums);

      for (int i = 0; i < nums.length - 2; i++) {
        int j = i + 1;
        int k = nums.length - 1;

        if (i != 0 && nums[i] == nums[i - 1]) {
          continue;
        }

        int sum = -nums[i];

        while (j < k) {
          int curSum = nums[j] + nums[k];
          if (curSum > sum) {
            k--;
          } else if (curSum < sum) {
            j++;
          } else {
            List<Integer> entry = new ArrayList<>();
            entry.add(nums[i]);
            entry.add(nums[j]);
            entry.add(nums[k]);

            solution.add(entry);
            j++;
            while (j < nums.length && nums[j] == nums[j - 1]) j++;
          }
        }
      }

      return solution;
    }
}
