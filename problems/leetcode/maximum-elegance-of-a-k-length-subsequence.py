# https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/
class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        # Sort items in the increasing order of profits.
        # This way, if we pick in order, we'd be maximizing profits.
        items.sort(key=lambda x: -x[0])

        elegance = 0
        duplicates = []
        total, categories = 0, set()

        # Compute elegance for the top k highest profits.
        for i in range(k):
            total += items[i][0]
            if items[i][1] in categories:
                duplicates.append(items[i][0])

            categories.add(items[i][1])

        elegance = total + (len(categories) ** 2)

        # For the remaining items, swap with the lowest duplicate profit item in
        # from duplicates iff it adds a unique category.
        for i in range(k, len(items)):
            if not duplicates:
                # We already have k unique items with the highest profit.
                break

            if items[i][1] not in categories:
                total += items[i][0] - duplicates.pop()
                categories.add(items[i][1])

                elegance = max(elegance, total + (len(categories) ** 2))

        return elegance
