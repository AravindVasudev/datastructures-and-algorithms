int houseRobber(int[] nums) {
    if (nums.length == 0) {
        return 0;
    }
    
    if (nums.length == 1) {
        return nums[0];
    }
    
    if (nums.length == 2) {
        return Math.max(nums[0], nums[1]);
    }
    
    int prevPrevMax = nums[0];
    int prevMax = Math.max(nums[0], nums[1]);
    int curMax = Integer.MIN_VALUE;
    for (int i = 2; i < nums.length; i++) {
        curMax = Math.max(prevMax, prevPrevMax + nums[i]);
        
        prevPrevMax = prevMax;
        prevMax = curMax;
    }
    
    return curMax;
}
