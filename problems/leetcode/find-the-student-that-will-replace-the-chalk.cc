// https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/
/*
Breakdown:
==========
- 0..N students.
- ith student use chalk[i].
- Go in circle.
- Ret: student who will replace chalk.

Brute Force:
============
i = 0
while true:
    if chalk[i] > k:
        ret i
    k -= chalk[i]
    i = (i + 1) % N, where N = len(chalk)

TC: O(k % sum(chalk)).
    - Eg: Say k = 22, sum(chalk) = 11, then it'd take around 2 walks.
SC: O(1).

Analysis:
=========
- If we know the sum of the array, we can skip unnecessary looping.

total = sum(chalk) # O(N)
k = k % total
for i, el in chalk: # O(N)
    if el > k:
        ret i
    
    k -= el

TC: O(N).
SC: O(1).

Minor Optimization:
===================
- If we compute prefix sum of the chalks, we can binary search for the
  student right away.

TC: O(N), for computing prefix sum (vs. O(2 * N), could be slightly faster irl based on the memory layout).
SC: O(N), for the prefix sum (this can be avoided by overwriting the array).
*/
class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        // Convert to prefix sum.
        const int N = chalk.size();
        vector<long> prefixSum(N);

        prefixSum[0] = chalk[0];
        for (int i = 1; i < N; i++) {
            prefixSum[i] += prefixSum[i - 1] + chalk[i];
        }

        // Remove any unnecessary rotations.
        if (k >= prefixSum.back()) {
            k %= prefixSum.back();
        }

        // Binary search for the smallest value
        // that's larger than k.
        size_t left = 0, right = N - 1;
        while (left < right) {
            size_t mid = (left + right) / 2;
            if (prefixSum[mid] > k) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }
};
