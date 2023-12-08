 # https://leetcode.com/problems/number-of-provinces/
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        visited = [False] * N

        def dfs(node):
            if visited[node]:
                return

            visited[node] = True
            for i in range(N):
                if isConnected[node][i]:
                    dfs(i)

        province = 0
        for node in range(N):
            if not visited[node]:
                dfs(node)
                province += 1

        return province
