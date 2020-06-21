# https://leetcode.com/problems/check-if-n-and-its-double-exist/
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        cache = set()
        for i in arr:
            if (2 * i) in cache or (i / 2) in cache:
                return True
            
            cache.add(i)
            
        return False
