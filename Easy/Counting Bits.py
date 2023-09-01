class Solution:
    def countBits(self, n: int) -> list[int]:
        res = []
        for i in range(0, n + 1):
            res.append(list(bin(i)).count("1"))
        return res
