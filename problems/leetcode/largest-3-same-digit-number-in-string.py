class Solution:
    def largestGoodInteger(self, num: str) -> str:
        goodInteger = "-1"

        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                substr = num[i:i+3]
                if int(substr) > int(goodInteger):
                    goodInteger = substr

        return goodInteger if goodInteger != "-1" else ""
