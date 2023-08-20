class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) != 1:
            res = [int(i) for i in str(num)]
            num = sum(res)
        return num