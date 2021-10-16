# https://leetcode.com/problems/employee-free-time/
# Approach 1: O(N log N), where N = number of total intervals
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        combined = [interval for person in schedule for interval in person]
        combined.sort(key=lambda x: x.start)
        
        res, prevEnd = [], combined[0].end
        for i in range(1, len(combined)):
            if prevEnd < combined[i].start:
                res.append(Interval(prevEnd, combined[i].start))
                
            prevEnd = max(prevEnd, combined[i].end)
            
        return res
      
# Efficient 1 (Merge Sort): O(N log K), where K = number of people
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        combined = self.mergeSort(schedule)
        
        free = []
        prevEnd = combined[0].end
        for i in range(1, len(combined)):
            if prevEnd < combined[i].start:
                free.append(Interval(prevEnd, combined[i].start))
                
            prevEnd = max(prevEnd, combined[i].end)
            
        return free
        
    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr[0]
        
        mid = len(arr) // 2
        
        left = self.mergeSort(arr[:mid])
        right = self.mergeSort(arr[mid:])
        
        return self.merge(left, right)
    
    def merge(self, left, right):
        combined = []
        
        leftPtr, rightPtr = 0, 0
        while leftPtr < len(left) and rightPtr < len(right):
            if left[leftPtr].start < right[rightPtr].start:
                combined.append(left[leftPtr])
                leftPtr += 1
            else:
                combined.append(right[rightPtr])
                rightPtr += 1
                
        combined += left[leftPtr:]
        combined += right[rightPtr:]
        
        return combined
        
# Efficient 2 (Priority Queue): O(N log K)
from dataclasses import dataclass

@dataclass
class Person:
    slots: List['Interval']
    index: int = 0
    
    def __lt__(self, other: 'Interval'):
        return self.getCurSlot().start < other.getCurSlot().start
    
    def getCurSlot(self):
        return self.slots[self.index]

    
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        heap = []

        for person in schedule:
            heapq.heappush(heap, Person(person))
        
        free = []
        prevEnd = heap[0].slots[0].end
        
        while heap:
            curPerson = heapq.heappop(heap)
            curSlot = curPerson.getCurSlot()
            
            if prevEnd < curSlot.start:
                free.append(Interval(prevEnd, curSlot.start))
            
            prevEnd = max(prevEnd, curSlot.end)
            
            if len(curPerson.slots) > curPerson.index + 1:
                curPerson.index += 1
                heapq.heappush(heap, curPerson)
                
        return free
