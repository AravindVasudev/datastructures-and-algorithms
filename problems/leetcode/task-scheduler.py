# https://leetcode.com/problems/task-scheduler/
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1: Build a max-heap of the tasks
        counts = Counter(tasks)
        heap = [-f for f in counts.values()]
        heapq.heapify(heap)

        time = 0
        cooldown = deque() # store items cooling down.
        while heap or cooldown:
            time += 1

            if heap:
                freq = heapq.heappop(heap) + 1 # Use one.
                if freq != 0:
                    cooldown.append((time + n, freq)) # Add to the cooldown queue.

            if cooldown and cooldown[0][0] == time:
                # If cooled down, move back to max-heap.
                _, freq = cooldown.popleft()
                heapq.heappush(heap, freq)

        return time
