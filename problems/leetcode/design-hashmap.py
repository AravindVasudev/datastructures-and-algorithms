# https://leetcode.com/problems/design-hashmap/
class MyHashMap:

    def __init__(self):
        self.numBuckets = 1000
        self.buckets = [[] for _ in range(self.numBuckets)]

    def put(self, key: int, value: int) -> None:
        self.remove(key)
        self.buckets[key % self.numBuckets].append((key, value))
        
    def get(self, key: int) -> int:
        bucket = self.buckets[key % self.numBuckets]
        for k, v in bucket:
            if key == k:
                return v
            
        return -1
        

    def remove(self, key: int) -> None:
        bucket = self.buckets[key % self.numBuckets]
        for i, (k, _) in enumerate(bucket):
            if key == k:
                del bucket[i]
