# https://leetcode.com/problems/valid-word-abbreviation/
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        w, a = 0, 0
        while w < len(word) and a < len(abbr):
            if word[w] == abbr[a]:
                w += 1
                a += 1
            elif abbr[a].isdigit() and abbr[a] != "0":
                index = a
                while index < len(abbr) and abbr[index].isdigit():
                    index += 1

                w += int(abbr[a:index])
                a = index
            else:
                return False

        return w == len(word) and a == len(abbr)
