# https://leetcode.com/problems/implement-trie-prefix-tree/
from dataclasses import dataclass, field

@dataclass
class TrieNode:
    children: defaultdict = field(default_factory=lambda: defaultdict(TrieNode))
    isLeaf: bool = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            cur = cur.children[char]
            
        cur.isLeaf = True
        cur.word = word
        

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            cur = cur.children.get(char)
            if cur is None:
                return False
            
        return cur.isLeaf
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            cur = cur.children.get(char)
            if cur is None:
                return False
            
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
