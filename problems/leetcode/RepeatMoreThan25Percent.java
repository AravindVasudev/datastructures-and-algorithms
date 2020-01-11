// https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
class Solution {
    public int findSpecialInteger(int[] arr) {
        int minRepeat = arr.length / 4;

        Map<Integer, Integer> count = new HashMap<>();
        for (int i : arr) {
            int newCount = count.getOrDefault(i, 0) + 1;
            count.put(i, newCount);
            if (newCount > minRepeat) {
                return i;
            }
        }

        return -1;
    }
}
