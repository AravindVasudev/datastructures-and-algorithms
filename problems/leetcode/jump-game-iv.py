# https://leetcode.com/problems/jump-game-iv/
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        N = len(arr)
        if N <= 1:
            return 0

        # Construct graph.
        graph = defaultdict(list)
        for i in range(N):
            graph[arr[i]].append(i)


        # Level-Order BFS.
        q = deque([0])
        visited = set()
        level = 0

        while q:
            levelSize = len(q)
            for _ in range(levelSize):
                node = q.popleft()
                if node == N - 1:
                    return level

                visited.add(node)

                # Add direct child, i.e., duplicates.
                for child in graph[arr[node]]:
                    if child not in visited:
                        q.append(child)

                # Add neighbor child.
                for child in (node - 1, node + 1):
                    if 0 <= child < N and child not in visited:
                        q.append(child)

                # Clear list to prevent redundant searches.
                graph[arr[node]].clear()

            level += 1

        return -1
