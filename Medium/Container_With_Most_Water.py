class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_v = 0
        i, j = 0, len(height) - 1
        while i < j:
            if height[i] < height[j]:
                max_v = max(max_v, height[i] * (j - i))
                i += 1
            else:
                max_v = max(max_v, height[j] * (j - i))
                j -= 1
        return max_v