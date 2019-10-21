class Solution {
    public boolean canJump(int[] nums) {
      if (nums.length == 0 || nums.length == 1) {
        return true;
      }

      int N = nums.length;
      int[] path = new int[N];

      for (int i = 0; i < N; i++) {
        int endRange = i + 1 + nums[i];
        for (int j = i + 1; j < N && j < endRange; path[j++]++);
      }

      for (int i = 1; i < N; i++) {
        if (path[i] == 0) {
          return false;
        }
      }

      return true;
    }
}
