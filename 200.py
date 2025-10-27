from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Handle empty input
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(sr: int, sc: int) -> None:
            q = deque([(sr, sc)])
            visit.add((sr, sc))
            while q:
                r, c = q.popleft()
                for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == "1" and
                        (nr, nc) not in visit
                    ):
                        visit.add((nr, nc))
                        q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands
