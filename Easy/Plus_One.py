class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = ""
        for i in digits:
            num += str(i)
        return [int(i) for i in str(int(num)+1)]