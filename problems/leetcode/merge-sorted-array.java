// https://leetcode.com/problems/merge-sorted-array/
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int num1Tail = m - 1, num2Tail = n - 1;
        int arrTail = (m + n) - 1;
        
        while (num1Tail >= 0 || num2Tail >= 0) {
            if (num1Tail >= 0 && num2Tail >= 0) {
                if (nums1[num1Tail] > nums2[num2Tail]) {
                    nums1[arrTail--] = nums1[num1Tail--];
                } else {
                    nums1[arrTail--] = nums2[num2Tail--];
                }
            } else if (num1Tail >= 0) {
                nums1[arrTail--] = nums1[num1Tail--];
            } else {
                nums1[arrTail--] = nums2[num2Tail--];
            }
        }
    }
}
