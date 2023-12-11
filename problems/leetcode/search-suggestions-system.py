# https://leetcode.com/problems/search-suggestions-system/
from dataclasses import field, dataclass

@dataclass
class TrieNode:
    children: defaultdict = field(default_factory=lambda: defaultdict(TrieNode))
    isLeaf: str = None
    words: List[str] = field(default_factory=lambda: [])

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        self.addList(words)

    def add(self, word):
        cur = self.root
        for c in word:
            cur = cur.children[c]
            cur.words.append(word)
            cur.words.sort()

        cur.isLeaf = word

    def addList(self, words):
        for word in words:
            self.add(word)

    def getTopThree(self, prefix):
        cur = self.root
        for c in prefix:
            cur = cur.children.get(c)
            if not cur:
                return []

        # results = sorted(self.getWords(cur, []))
        # return results[:3] if len(results) > 3 else results
        return cur.words[:3] if len(cur.words) > 3 else cur.words


    # def getWords(self, head, results):
    #     if head.isLeaf:
    #         results.append(head.isLeaf)

    #     for node in head.children.values():            
    #         self.getWords(node, results)

    #     return results


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie(products)
        
        result = []
        for i in range(len(searchWord)):
            result.append(trie.getTopThree(searchWord[:i+1]))

        return result
