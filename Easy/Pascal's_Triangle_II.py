class Solution:
    def getRow(self, numRows: int) -> list[list[int]]:
        binom = [0]*(numRows+1)
        binom[0] = 1
        for i in range(1, numRows + 1):
            for j in range(i, 0, -1):
                binom[j] += binom[j-1]
        return binom