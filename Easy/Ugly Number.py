class Solution:
    def isUgly(self, n: int) -> bool:

        if n == 1:
            return True
        while n > 1:
            if n % 2 == 0:
                n /= 2
            if n % 3 == 0:
                n /= 3
            if n % 5 == 0:
                n /= 5
            if n == 1:
                return True
            if n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
                break
        return False