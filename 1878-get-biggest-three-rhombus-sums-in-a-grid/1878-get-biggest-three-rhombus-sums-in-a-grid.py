from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        s = set()

        # Rhombus of size 0
        for row in grid:
            for x in row:
                s.add(x)

        for r in range(m):
            for c in range(n):
                k = 1
                while r + 2 * k < m and c - k >= 0 and c + k < n:
                    total = 0

                    # top -> right
                    for i in range(k):
                        total += grid[r + i][c + i]

                    # right -> bottom
                    for i in range(k):
                        total += grid[r + k + i][c + k - i]

                    # bottom -> left
                    for i in range(k):
                        total += grid[r + 2 * k - i][c - i]

                    # left -> top
                    for i in range(k):
                        total += grid[r + k - i][c - k + i]

                    s.add(total)
                    k += 1

        return sorted(s, reverse=True)[:3]