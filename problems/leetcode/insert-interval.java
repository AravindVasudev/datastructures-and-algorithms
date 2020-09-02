// https://leetcode.com/problems/insert-interval/
class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> intervalList = new LinkedList<>();
        
        int i = 0;
        while (i < intervals.length && intervals[i][1] < newInterval[0]) {
            intervalList.add(intervals[i++]);
        }
        
        while (i < intervals.length && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = Math.min(intervals[i][0], newInterval[0]);
            newInterval[1] = Math.max(intervals[i][1], newInterval[1]);
            
            i++;
        }
        
        intervalList.add(newInterval);
        
        while (i < intervals.length) {
            intervalList.add(intervals[i++]);
        }
        
        return intervalList.toArray(new int[0][2]);
    }
}
