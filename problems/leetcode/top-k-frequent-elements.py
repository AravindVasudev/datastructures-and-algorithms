# https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        
        pqueue = []
        for element, count in counter.items():
            heapq.heappush(pqueue, (count, element))
            
            if len(pqueue) > k:
                heapq.heappop(pqueue)
                
        return [element for _, element in pqueue]

# O(N) bucket sort solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return [e for e, _ in Counter(nums).most_common(k)]
        counter = Counter(nums)

        # Bucket sort the results.
        buckets = [[] for _ in range(len(nums))]
        for el, count in counter.items():
            buckets[count - 1].append(el)

        # Pick top-k elements.
        result = []
        for i in reversed(range(len(nums))):
            if buckets[i]:
                result.extend(buckets[i])

            if len(result) >= k:
                break

        return result[:k]
