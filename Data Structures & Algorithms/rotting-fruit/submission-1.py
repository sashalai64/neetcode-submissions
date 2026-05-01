class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0
        q = deque()
        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
                    visited.add((i, j))

        time = 0
        # if no fresh fruit we don't have to count anymore
        while q and fresh:
            time += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    x, y = i + dx, j + dy
                    if x >= 0 and x < m and y >= 0 and y < n and (x, y) not in visited and grid[x][y] == 1:
                        q.append((x, y))
                        visited.add((x, y))
                        fresh -= 1
                        grid[x][y] = 2
        
        return time if fresh == 0 else -1
        



