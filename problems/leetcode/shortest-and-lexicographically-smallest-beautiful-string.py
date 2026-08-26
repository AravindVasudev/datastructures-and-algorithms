# https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        N = len(s)
        start, window = 0, 0
        string = ""

        for end in range(N):
            while start < N and s[start] != "1":
                start += 1 # Start at one.

            # if start == N: break
            if s[end] == "1":
                window += 1 # Update counter if 1 is added.

            if window == k:
                length = end - start + 1
                substr = s[start:end+1]
                if string == "" or len(string) > length:
                    string = substr
                elif string != "" and len(string) == length and string > substr:
                    string = substr

                start += 1
                window -= 1

        return string
