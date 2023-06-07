class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a > 0 or b > 0 or c > 0:
            bit_a, bit_b, bit_c = a & 1, b & 1, c & 1
            if bit_c == 0:
                flips += bit_a + bit_b
            else:
                flips += 1 if bit_a == bit_b == 0 else 0
            a, b, c = a >> 1, b >> 1, c >> 1
        return flips