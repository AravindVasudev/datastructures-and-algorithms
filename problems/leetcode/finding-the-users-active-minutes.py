# https://leetcode.com/problems/finding-the-users-active-minutes/
from collections import defaultdict

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        userVsMin = defaultdict(set)
        for log in logs:
            userVsMin[log[0]].add(log[1])

        uamCount = [0] * k
        for user, mins in userVsMin.items():
            count = len(mins)
            if count <= k:
                uamCount[count - 1] += 1

        return uamCount
