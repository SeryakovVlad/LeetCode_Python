# class Solution:
#     def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
#         result = []
#         index = 0
#         while index + k != len(nums) + 1:
#             result.append(max(nums[index:index+k]))
#             index += 1
#         return result


from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        result = []
        window = deque()
        
        for i, num in enumerate(nums):
            
            while window and window[0] < i - k + 1:
                window.popleft()
            
            
            while window and nums[window[-1]] < num:
                window.pop()
            
            window.append(i)
            
            if i >= k - 1:
                result.append(nums[window[0]])
        
        return result