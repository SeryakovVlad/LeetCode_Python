class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        dict_below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                    "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        dict_tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        dict_thousands = ["", "Thousand", "Million", "Billion"]

        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return dict_below_20[n] + " "
            elif n < 100:
                return dict_tens[n // 10] + " " + helper(n % 10)
            else:
                return dict_below_20[n // 100] + " Hundred " + helper(n % 100)
        
        words = ""
        i = 0
        while num > 0:
            if num % 1000 != 0:
                if words:
                    words = helper(num % 1000) + dict_thousands[i] + " " + words
                else:
                    words = helper(num % 1000) + dict_thousands[i]
            num //= 1000
            i += 1
        return words.strip()