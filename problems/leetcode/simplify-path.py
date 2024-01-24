# https://leetcode.com/problems/simplify-path/
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for segment in path.split("/"):
            if not segment or segment == ".":
                continue

            if segment == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(segment)

        return "/" + "/".join(stack)
