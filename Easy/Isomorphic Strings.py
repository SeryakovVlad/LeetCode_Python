class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            char_map = {}
            chars = set()
            for i in range(len(s)):
                if s[i] in char_map:
                    if char_map[s[i]] != t[i]:
                        return False
                else:
                    if t[i] in chars:
                        return False
                    char_map[s[i]] = t[i]
                    chars.add(t[i])
            return True
        return False