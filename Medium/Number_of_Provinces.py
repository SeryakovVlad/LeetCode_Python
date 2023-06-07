class Solution:
    def findCircleNum(self, isConnected) -> int:
        def dfs(i):
            for j in range(n):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)

        n = len(isConnected)
        visited = set()
        provinces = 0

        for i in range(n):
            if i not in visited:
                dfs(i)
                provinces += 1

        return provinces