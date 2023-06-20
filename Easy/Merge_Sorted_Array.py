
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> list:
        p1 = len(nums1) - m
        while p1 != 0:
            nums1.pop()
            p1 -= 1
        p2 = len(nums2) - n
        while p2 != 0:
            nums2.pop()
            p2 -= 1
        nums1 += nums2
        nums1.sort()
        return nums1
print(Solution().merge([-1,0,0,3,3,3,0,0,0],6,[1,2,2],3))