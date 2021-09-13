# https://leetcode.com/problems/peeking-iterator/

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        
        self.iterator = iterator
        self.seen = deque()
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        
        if not self.seen:
            self.seen.append(self.iterator.next())
            
        return self.seen[0]

    def next(self):
        """
        :rtype: int
        """
        
        if self.seen:
            return self.seen.popleft()
        
        return self.iterator.next()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        
        if self.seen:
            return True
        
        return self.iterator.hasNext()


# Efficient
class PeekingIterator:
    def __init__(self, iterator):
        self.iter = iterator
        self.buffer = self.iter.next() if self.iter.hasNext() else None

    def peek(self):
        return self.buffer

    def next(self):
        ret = self.buffer
        self.buffer = self.iter.next() if self.iter.hasNext() else None
        
        return ret

    def hasNext(self):
        return self.buffer is not None
