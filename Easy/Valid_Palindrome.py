class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ''.join(ch.lower() for ch in s if ch.isalpha() or ch.isdigit())
        return text == text[::-1]