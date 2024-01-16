# https://leetcode.com/problems/design-in-memory-file-system/
from dataclasses import dataclass, field

@dataclass
class Node:
    child: defaultdict["Node"] = field(default_factory=lambda: defaultdict(Node))
    content: str = ""

class FileSystem:

    def __init__(self):
        self.root = Node()

    def _find(self, path: str, createPath: bool = True) -> Node:
        if len(path) == 1:
            return self.root

        cur = self.root
        for word in path.split("/")[1:]:
            if not createPath and word not in cur.child:
                return None
    
            cur = cur.child[word]

        return cur
        

    def ls(self, path: str) -> List[str]:
        node = self._find(path, createPath=False)
        if node.content:
            return [path.split("/")[-1]]

        return sorted(node.child.keys())
        

    def mkdir(self, path: str) -> None:
        self._find(path)
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self._find(filePath)
        node.content += content
        

    def readContentFromFile(self, filePath: str) -> str:
        node = self._find(filePath)
        return node.content 
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
