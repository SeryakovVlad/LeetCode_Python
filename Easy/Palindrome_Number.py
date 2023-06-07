class Solution:
    def isPalindrome(self, word: int) -> bool:
        return str(word) == str(word)[::-1]