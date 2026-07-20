class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(grid),len(grid[0])
        total = m*n
        k %= total

        flat = []
        for r in range(m):
            for c in range(n):
                flat.append(grid[r][c])

        flat = flat[-k:] + flat[:-k]

        res = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(flat[i * n + j])
            res.append(row)

        return res