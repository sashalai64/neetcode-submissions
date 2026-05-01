class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rot = deque()
        visited = set()
        fresh = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rot.append((i, j))
                    visited.add((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        time = 0
        while rot and fresh:
            time += 1
            for _ in range(len(rot)):
                i, j = rot.popleft()
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1 and (x, y) not in visited:
                        grid[x][y] = 2
                        fresh -= 1
                        rot.append((x, y))
                        visited.add((x, y))


        return time if fresh == 0 else -1


