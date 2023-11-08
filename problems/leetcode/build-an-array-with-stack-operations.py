class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        output = []

        stream = 1
        for el in target:
            while stream < el:
                output.append("Push")
                output.append("Pop")
                stream += 1

            output.append("Push")
            stream += 1

        return output
