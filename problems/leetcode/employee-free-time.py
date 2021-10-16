# https://leetcode.com/problems/employee-free-time/
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
      
# Efficient
