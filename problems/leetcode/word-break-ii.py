# https://leetcode.com/problems/word-break-ii/
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        return self.dfs(s, wordSet, "", [])
    
    def dfs(self, s: str, wordSet: set[str], path: str, result: List[str]) -> List[str]:
        if s == "":
            result.append(path.strip())
            return
        
        for i in range(1, len(s) + 1):
            if s[:i] in wordSet:
                self.dfs(s[i:], wordSet, f"{path} {s[:i]}", result)
                
        return result

# Optimized
# With DP memo
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        return self.dfs(s, wordSet, {})
    
    def dfs(self, s: str, wordSet: set[str], memo: Dict[str, List[str]]) -> List[str]:            
        if s in memo:
            return memo[s]
        
        if s == "":
            return [""]
        
        result = []
        for i in range(1, len(s) + 1):
            word = s[:i]
            if word in wordSet:
                result.extend([word + (" " if suffix else "") + suffix for suffix in self.dfs(s[i:], wordSet, memo)])
                
        memo[s] = result
        return result
