# class Solution:
#     def divide(self, dividend: int, divisor: int) -> int:
#         n = 0
#         if dividend >=0 and divisor >= 0:
#             while dividend >= divisor:
#                 dividend -= divisor
#                 n += 1
#             return n
#         elif dividend < 0 and divisor > 0:
#             while dividend <= -divisor:
#                 dividend += divisor
#                 n -= 1
#             return n
#         elif dividend > 0 and divisor < 0:
#             while dividend >= -divisor:
#                 dividend += divisor
#                 n -= 1
#             return n
#         else:
#             while dividend <= divisor:
#                 dividend -= divisor
#                 n += 1
#             return n

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0

        while dividend >= divisor:
            current_divisor = divisor
            multiple = 1

            while dividend >= (current_divisor << 1):
                current_divisor <<= 1
                multiple <<= 1

            dividend -= current_divisor
            quotient += multiple

        if negative:
            quotient = -quotient

        return max(min(quotient, INT_MAX), INT_MIN)
