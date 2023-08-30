# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         for i in nums:
#             if nums.count(i) != 1:
#                 return True
#         return False

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False