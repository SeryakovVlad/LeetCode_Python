class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        prev = self.countAndSay(n-1)

        res = []

        count = 1
        for i in range(len(prev)):
            if i + 1 < len(prev) and prev[i] == prev[i + 1]:
                count += 1
            else:
                res.append(str(count) + prev[i])
                count = 1

        return "".join(res) 

print(Solution().countAndSay(5))