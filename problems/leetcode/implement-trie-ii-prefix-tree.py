# https://leetcode.com/problems/implement-trie-ii-prefix-tree/
from dataclasses import dataclass, field

@dataclass
class TrieNode:
    children: defaultdict = field(default_factory=lambda: defaultdict(TrieNode))
    count: int = 0
    countStartsWith: int = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            cur = cur.children[char]
            cur.countStartsWith += 1
            
        cur.count += 1
        

    def countWordsEqualTo(self, word: str) -> int:
        cur = self.root
        for char in word:
            cur = cur.children[char]
            
        return cur.count
        

    def countWordsStartingWith(self, prefix: str) -> int:
        cur = self.root
        for char in prefix:
            cur = cur.children[char]
            
        return cur.countStartsWith

    def erase(self, word: str) -> None:
        cur = self.root
        for char in word:
            cur = cur.children[char]
            cur.countStartsWith -= 1
        
        cur.count -= 1
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
