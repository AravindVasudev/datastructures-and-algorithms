class Solution {
    public boolean canJump(int[] nums) {
      if (nums.length == 0 || nums.length == 1) {
        return true;
      }

      int N = nums.length;
      boolean[] path = new boolean[N];

      path[0] = true;
      for (int i = 0; i < N; i++) {
        if (!path[i]) {
          return false;
        }

        int endRange = i + 1 + nums[i];
        for (int j = i + 1; j < N && j < endRange; j++) {
          path[j] = true;
        }

        if (path[N - 1]) {
          return true;
        }
      }

      return true;
    }
}

