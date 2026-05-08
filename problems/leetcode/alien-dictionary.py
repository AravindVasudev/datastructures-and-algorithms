# https://leetcode.com/problems/alien-dictionary/
from collections import defaultdict, deque
from typing import List


class Solution:
    def constructOrderingGraph(
        self, words: List[str]
    ) -> tuple[dict[str, set[str]], dict[str, int]]:

        graph = defaultdict(set)
        indegree = {c: 0 for word in words for c in word}

        for i in range(1, len(words)):
            w1, w2 = words[i - 1], words[i]

            # Invalid prefix case
            if len(w1) > len(w2) and w1.startswith(w2):
                return {}, {}

            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1

                    # Only first differing character matters
                    break

        return graph, indegree

    def topologicalSort(
        self,
        graph: dict[str, set[str]],
        indegree: dict[str, int]
    ) -> list[str]:

        queue = deque([c for c in indegree if indegree[c] == 0])
        result = []

        while queue:
            c = queue.popleft()
            result.append(c)

            for neighbor in graph[c]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Cycle detected
        if len(result) != len(indegree):
            return []

        return result

    def alienOrder(self, words: List[str]) -> str:
        graph, indegree = self.constructOrderingGraph(words)

        # Invalid prefix case
        if not indegree and words:
            return ""

        ordering = self.topologicalSort(graph, indegree)

        return "".join(ordering)
