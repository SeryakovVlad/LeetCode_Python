class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        delta = arr[1] - arr[0]
        for i in range(0, len(arr)-1):
            if arr[i] + delta != arr[i+1]:
                return False
        return True