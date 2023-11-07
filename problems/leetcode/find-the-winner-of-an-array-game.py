"""
Rules:
======
1. Compare arr[0] & arr[1].
2. Largest wins.
3. Move smaller to the end of the array.
4. If arr[0] wins k times, game ends.

Brute Force:
============
1. Reshuffle array, i.e., pop loser and move to the end.
2. Maintain a score map for each el, update index when they move.

TC: O(N^2)
SC: O(1)

Observations:
=============
1. Comparision only happens b/w two el at any given time.
2. We require removing el in the front of the array.
3. We require adding el to the back of the array.
---> Maybe use a queue?

Optimization:
=============
1. winner = arr[0], winning = 0.
2. Enqueue arr[1..n] to a queue.
3. While winning < k:
    3.1. pop queue.
    3.2. compare winner & pop.
        3.2.1. If winner, winning++
        3.2.2. If winner loses, replace winner & enqueue loser.
"""

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        max_el = max(arr)
        winner = arr[0]
        winning = 0
        q = deque(arr[1:])

        while winning < k:
            nxt = q.popleft()
            if winner > nxt:
                q.append(nxt)
                winning += 1
            else:
                q.append(winner)
                winner = nxt
                winning = 1

            if winner == max_el:
                break

        return winner
