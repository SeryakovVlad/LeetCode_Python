class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] < target and i != j:
                    count += 1
        return count