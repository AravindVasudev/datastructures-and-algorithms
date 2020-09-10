// https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/
/**
 * // This is ArrayReader's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface ArrayReader {
 *     public int get(int index) {}
 * }
 */

class Solution {
    public int search(ArrayReader reader, int target) {
        if (reader.get(0) == target) {
            return 0;
        }
        
        // Binary search for bound
        int left = 0, right = 1;
        while (reader.get(right) < target) {
            left = right;
            right <<= 1;
        }
        
        // Binary search the value
        while (left <= right) {
            int midIndex = (left + right) / 2;
            int mid = reader.get(midIndex);
            
            if (mid == target) {
                return midIndex;
            } else if (mid < target) {
                left = midIndex + 1;
            } else {
                right = midIndex - 1;
            }
        }
        
        return -1;
    }
}
