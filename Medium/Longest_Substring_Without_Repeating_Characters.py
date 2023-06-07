class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left = right = max_length = 0
        while right < len(s):
            if s[right] not in chars:
                chars.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                chars.remove(s[left])
                left += 1
        return max_length