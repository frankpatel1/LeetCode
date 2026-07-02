from collections import deque

class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        # min_loss[i][j] stores the minimum health points lost to reach (i, j)
        min_loss = [[float('inf')] * n for _ in range(m)]
        min_loss[0][0] = grid[0][0]
        
        # Deque for 0-1 BFS: stores (row, col)
        q = deque([(0, 0)])
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while q:
            r, c = q.popleft()
            
            # If we reached the destination, we can exit early if we want,
            # but 0-1 BFS ensures we find the shortest path cleanly.
            if r == m - 1 and c == n - 1:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    next_loss = min_loss[r][c] + grid[nr][nc]
                    
                    # If we found a path with fewer health losses
                    if next_loss < min_loss[nr][nc]:
                        min_loss[nr][nc] = next_loss
                        # 0-1 BFS optimization
                        if grid[nr][nc] == 0:
                            q.appendleft((nr, nc)) # Cost 0 -> Front
                        else:
                            q.append((nr, nc))     # Cost 1 -> Back
                            
        # Check if the remaining health is at least 1
        return min_loss[m - 1][n - 1] < health