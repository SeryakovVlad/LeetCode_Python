class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged_arr = nums1 + nums2
        merged_arr.sort()
        index = (len(merged_arr) - 1) / 2
        if int(index) == index:
            res = merged_arr[int(index)]
        else:
            res = (merged_arr[int(index - 0.5)] + merged_arr[int(index + 0.5)]) / 2
        return res
    
print(Solution().findMedianSortedArrays([1, 3], [2]))