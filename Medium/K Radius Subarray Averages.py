class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        avgs = [-1] * n

        # Calculate prefix sum
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        # Calculate k-radius average for each valid index
        for i in range(k, n - k):
            avgs[i] = (prefix_sum[i + k + 1] - prefix_sum[i - k]) // (2 * k + 1)

        return avgs
