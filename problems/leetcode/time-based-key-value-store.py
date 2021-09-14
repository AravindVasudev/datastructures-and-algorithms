# https://leetcode.com/problems/time-based-key-value-store/
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        # List because timestamp is strictly increasing
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        keys = self.store[key]

        left, right = 0, len(keys) - 1
        while left < right:
            mid = (left + right + 1) // 2
            
            if keys[mid][1] == timestamp:
                return keys[mid][0]
            elif keys[mid][1] > timestamp:
                right = mid - 1
            else:
                left = mid
                
        return keys[left][0] if 0 <= left < len(keys) and keys[left][1] <= timestamp else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
