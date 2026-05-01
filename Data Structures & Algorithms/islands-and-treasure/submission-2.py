class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        q = deque()
        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))
        step = 0
        while q:
            step += 1
            for _ in range(len(q)):
                i, j = q.popleft()

                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    x, y = i + dx, j + dy
                    if x >= 0 and x < m and y >= 0 and y < n and grid[x][y] != -1 and (x, y) not in visited:
                        grid[x][y] = step
                        q.append((x, y))
                        visited.add((x, y))
        
            