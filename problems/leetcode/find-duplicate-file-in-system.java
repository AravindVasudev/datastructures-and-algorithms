//https://leetcode.com/problems/find-duplicate-file-in-system/
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        fileMap = defaultdict(list)
        
        for path in paths:
            pathItems = path.split(" ")
            location, files = pathItems[0], pathItems[1:]
            
            for file in files:
                filename, content = file.split("(")
                content = content[:-1]
            
                fileMap[content].append("{}/{}".format(location, filename))
            
        result = []
        for k, v in fileMap.items():
            if len(v) > 1:
                result.append(v)
                
        return result
