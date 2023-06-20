class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        available_plots = 0
        consecutive_zeros = 0
        for plot in flowerbed:
            if plot == 0:
                consecutive_zeros += 1
            else:
                available_plots += (consecutive_zeros - 1) // 2
                consecutive_zeros = 0

        if consecutive_zeros > 0:
            available_plots += (consecutive_zeros - 1) // 2

        return available_plots >= n