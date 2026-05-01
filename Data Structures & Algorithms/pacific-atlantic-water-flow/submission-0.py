class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(i, j, prev, visited):
            if i < 0 or i >= m or j < 0 or j >= n or heights[i][j] < prev or (i, j) in visited:
                return
            
            visited.add((i, j))
            dfs(i - 1, j, heights[i][j], visited)
            dfs(i + 1, j, heights[i][j], visited)
            dfs(i, j - 1, heights[i][j], visited)
            dfs(i, j + 1, heights[i][j], visited)
        
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dfs(i, j, heights[i][j], pacific)

                if i == m - 1 or j == n - 1:
                    dfs(i, j, heights[i][j], atlantic)
        
        res = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append([i, j])
        
        return res
        