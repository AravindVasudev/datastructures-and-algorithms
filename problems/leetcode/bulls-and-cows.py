# https://leetcode.com/problems/bulls-and-cows/
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        
        secretMap = defaultdict(set)
        for i, char in enumerate(secret):
            secretMap[char].add(i)
            
        for i, char in enumerate(guess):
            if char in secretMap and len(secretMap[char]):
                if i in secretMap[char]:
                    bulls += 1
                    secretMap[char].remove(i)
                else:
                    for x in secretMap[char]:
                        if guess[x] != char:
                            cows += 1
                            secretMap[char].remove(x)
                            break
                                      
        return f"{bulls}A{cows}B"
