# https://leetcode.com/problems/remove-duplicate-letters/
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen = set() # set of char in the stack.
        stack = []

        # The last occurence of each char.
        lastOccurence = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            # if already in the stack, ignore.
            if c in seen:
                continue

            # If top of the monotonic stack is > and that char will
            # occur again, remove it from the stack.
            while stack and c < stack[-1] and i < lastOccurence[stack[-1]]:
                seen.discard(stack.pop())

            # Add the char to the monotonic stack.
            seen.add(c)
            stack.append(c)

        return "".join(stack)
