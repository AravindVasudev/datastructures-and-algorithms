# https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ''

        prefix = ''
        for i in range(min(map(len, strs))):
            if not all([s[i] == strs[0][i] for s in strs]):
                break
                
            prefix += strs[0][i]
                
        return prefix
