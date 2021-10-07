# https://leetcode.com/problems/longest-absolute-file-path/
from dataclasses import dataclass, field

@dataclass
class Path:
    name: str
    children: List[any] = field(default_factory=list)

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # Generate Tree
        nodeDeque = deque(input.split("\n"))
        nodeDeque.appendleft('') # absolute root
        tree = self.generateTree(nodeDeque)
        
        # Find Longest Path
        path = self.longestPath(tree)
        return 0 if path == 0 else path - 1 # -1 for absolute root
    
    def generateTree(self, nodes: deque, depth: int = -1) -> Path:
        getDepth = lambda node: len(node) - len(node.strip('\t'))
        if len(nodes) == 0:
            return
        
        curNode = Path(nodes.popleft().strip('\t'))
        while len(nodes) and getDepth(nodes[0]) > depth:
            curNode.children.append(self.generateTree(nodes, depth + 1))
            
        return curNode
    
    def longestPath(self, node: Path) -> int:
        if node is None:
            return 0
        
        if node.name.find(".") != -1:
            return len(node.name)
        
        if len(node.children) == 0:
            return 0
        
        longestChild = max(map(self.longestPath, node.children))
        return  longestChild + (len(node.name) + 1 if longestChild > 0 else 0)
