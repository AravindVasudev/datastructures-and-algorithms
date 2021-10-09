# https://leetcode.com/problems/number-of-atoms/
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        atomMap = {}
        
        index = 0
        while index < len(formula):
            if formula[index] == "(":
                stack.append(atomMap)
                
                index += 1
                atomMap = {}
                continue
            
            if formula[index] == ")":
                prevAtomMap = stack.pop()
                index += 1
                
                currentCount = 0
                while index < len(formula) and formula[index].isdigit():
                    currentCount = currentCount * 10 + int(formula[index])
                    index += 1

                if currentCount != 0:
                    for key in atomMap:
                        atomMap[key] *= currentCount
                        
                for key, value in prevAtomMap.items():
                    if key in atomMap:
                        atomMap[key] += value
                    else:
                        atomMap[key] = value
                        
                continue
                
            currentAtom = formula[index]
            index += 1
            
            while index < len(formula) and formula[index].islower():
                currentAtom += formula[index]
                index += 1
                
            currentCount = 0
            while index < len(formula) and formula[index].isdigit():
                currentCount = currentCount * 10 + int(formula[index])
                index += 1
                
            if currentCount == 0:
                currentCount = 1
            
            if currentAtom in atomMap:
                atomMap[currentAtom] += currentCount
            else:
                atomMap[currentAtom] = currentCount
            
            
        result = ""
        for element in sorted(atomMap.keys()):
            if atomMap[element] > 1:
                result += f"{element}{atomMap[element]}"
            else:
                result += element
            
        return result
        
