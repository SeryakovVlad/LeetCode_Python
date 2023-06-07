class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        temp = []
        for i in nums:
            if i in temp:
                temp.remove(i)
            else:
                temp.append(i)
        return temp[0]