class Solution:
    def longestCommonPrefix(self, strs:list[str])->str:
        if not strs:
            return ""
        
        # Sort the list to compare the first and the last string
        strs.sort()
        
        prefix = ""
        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                prefix += strs[0][i]
            else:
                break
        return prefix