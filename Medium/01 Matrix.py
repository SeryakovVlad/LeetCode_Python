class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows = len(mat)
        columns = len(mat[0])
        MAX_INT = 10**9
        
        result = [[MAX_INT if mat[i][j] != 0 else 0 for j in range(columns)] for i in range(rows)]
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for i in range(rows):
            for j in range(columns):
                if mat[i][j] == 0:
                    continue

                for direction_i, direction_j in directions:
                    ni, nj = i + direction_i, j + direction_j
                    if 0 <= ni < rows and 0 <= nj < columns:
                        result[i][j] = min(result[i][j], result[ni][nj] + 1)
        
        for i in range(rows - 1, -1, -1):
            for j in range(columns - 1, -1, -1):
                if mat[i][j] == 0:
                    continue

                for direction_i, direction_j in directions:
                    ni, nj = i + direction_i, j + direction_j
                    if 0 <= ni < rows and 0 <= nj < columns:
                        result[i][j] = min(result[i][j], result[ni][nj] + 1)
        
        return result

print(Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))