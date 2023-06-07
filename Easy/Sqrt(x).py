class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        xn = x
        e = 1e-4
        while True:
            sqrt = 0.5 * (xn + x / xn)
            if abs(sqrt**2 - x) < e:
                return int(sqrt)
            xn = sqrt

print(Solution().mySqrt(1))