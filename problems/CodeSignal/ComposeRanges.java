String[] composeRanges(int[] nums) {
    int i = 0;
    List<String> output = new ArrayList<>();
    
    if (nums.length == 0) {
        return output.toArray(new String[0]);
    }
    
    for (int j = 1; j < nums.length; j++) {
        if (nums[j] != nums[j - 1] + 1) {
            if (j - 1 == i) {
                output.add(Integer.toString(nums[j - 1]));
            } else {
                output.add(String.format("%d->%d", nums[i], nums[j - 1]));
            }
            
            i = j;
        }
    }
    
    if (i == nums.length - 1) {
        output.add(Integer.toString(nums[i]));
    } else {
        output.add(String.format("%d->%d", nums[i], nums[nums.length - 1]));
    }
    
    return output.toArray(new String[0]);
}
