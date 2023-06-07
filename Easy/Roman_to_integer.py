class Solution:
    def romanToInt(self, s: str) -> int:
        value = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res, prev = 0, 0
        for i in s:
            curr = value[i]
            if prev < curr:
                res += curr - 2*prev
            else:
                res += curr
            prev = curr
        return res