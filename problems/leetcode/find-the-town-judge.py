# https://leetcode.com/problems/find-the-town-judge/
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incomingTrust = [0] * n
        outgoingTrust = [0] * n

        for trustVal in trust:
            incomingTrust[trustVal[1] - 1] += 1
            outgoingTrust[trustVal[0] - 1] += 1
           
        judge = -1
        for i in range(n):
            if incomingTrust[i] == n - 1 and outgoingTrust[i] == 0:
                if judge != -1:
                    return -1
                else:
                    judge = i + 1
                    
        return judge
        
