# https://leetcode.com/problems/design-file-system/
from dataclasses import dataclass, field

@dataclass
class FileNode:
    children: defaultdict["FileNode"] = field(default_factory=lambda: defaultdict(FileNode))
    value: int = -1


class FileSystem:

    def __init__(self):
        self.root = FileNode()

    def createPath(self, path: str, value: int) -> bool:
        cur = self.root
        pathComponents = path.split("/")[1:]
        for i, el in enumerate(pathComponents):
            if el not in cur.children and i != len(pathComponents) - 1:
                return False

            cur = cur.children[el]

        if cur.value != -1:
            return False

        cur.value = value
        return True

    def get(self, path: str) -> int:
        cur = self.root
        for el in path.split("/")[1:]:
            if el not in cur.children:
                return -1

            cur = cur.children[el]

        return cur.value
