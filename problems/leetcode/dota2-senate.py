# https://leetcode.com/problems/dota2-senate/
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
      count = Counter(senate)
      banned = {"R": 0, "D": 0}
      queue = deque(senate)

      while queue:
        senator = queue.popleft()
        if banned[senator] > 0:
          banned[senator] -= 1
          count[senator] -= 1
          continue

        if senator == "R" and count["D"] <= banned["D"]:
          return "Radiant"

        if senator == "D" and count["R"] <= banned["R"]:
          return "Dire"

        banned["D" if senator == "R" else "R"] += 1
        queue.append(senator)
