# https://leetcode.com/problems/asteroid-collision/
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # 5 ---> 10 ---> <--- -5 = [5, 10]
        # 8 ---> <--- -8 = []
        # 10 ---> 2 ---> <--- -5 = [10]
        # <--- 2 <--- 1 1 ---> 2 ---> = [-2, -1, 1, 2]
        
        prevCycle = asteroids
        while True:
            curCycle = []
            for i in range(len(prevCycle)): # one element?
                curAsteroid = prevCycle[i]
                if curAsteroid == 0:
                    continue
                
                if i + 1 >= len(prevCycle):
                    curCycle.append(curAsteroid)
                    continue
    
                nextAsteroid = prevCycle[i + 1]
                

                
                if (curAsteroid < 0 and nextAsteroid < 0) or \
                    (curAsteroid > 0 and nextAsteroid > 0) or \
                    (curAsteroid < 0 and nextAsteroid > 0):
                    curCycle.append(curAsteroid)
                    continue
                    
                curMagnitude = abs(curAsteroid)
                nextMagnitude = abs(nextAsteroid)
                
                if curMagnitude == nextMagnitude:
                    prevCycle[i] = 0
                    prevCycle[i + 1] = 0
                elif curMagnitude > nextMagnitude:
                    curCycle.append(curAsteroid)
                    prevCycle[i + 1] = 0
                else:
                    prevCycle[i] = 0
                    
            if prevCycle == curCycle:
                break
                
            prevCycle = curCycle
                
        return prevCycle
                    
