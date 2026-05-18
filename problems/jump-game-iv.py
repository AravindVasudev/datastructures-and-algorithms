# https://leetcode.com/problems/jump-game-iv/
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # 0: Edge case checks
        N = len(arr)
        if N == 1: # len(arr) cannot be 0.
            return 0

        # 1: Build graph.
        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)

        # 2: Setup BFS.
        queue = deque([0])
        visited = {0}
        level = 0

        # 3: Level-order traverse the graph from start.
        while queue:
            size = len(queue)
            for _ in range(size):
                index = queue.popleft()
                if index == N - 1:
                    return level # Found!

                # 3.1: Sibling left
                if index - 1 >= 0 and index - 1 not in visited:
                    visited.add(index - 1)
                    queue.append(index - 1)

                # 3.2: Sibling right
                if index + 1 < N and index + 1 not in visited:
                    visited.add(index + 1)
                    queue.append(index + 1)

                # 3.3: Same value siblings
                for sibling in graph[arr[index]]:
                    if sibling == index or sibling in visited:
                        continue # Already visited.

                    visited.add(sibling)
                    queue.append(sibling)

                # 4: Clear the adjacency list to prevent reiteration.
                # Everything here is already enqueued. 
                graph[arr[index]].clear()

            # Move next level.
            level += 1

        return -1
