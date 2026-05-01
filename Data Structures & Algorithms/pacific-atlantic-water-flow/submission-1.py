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
            dfs(i, 0, heights[i][0], pacific)
            dfs(i, n - 1, heights[i][n - 1], atlantic)
        
        for j in range(n):
            dfs(0, j, heights[0][j], pacific)
            dfs(m - 1, j, heights[m - 1][j], atlantic)
        
        res = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append([i, j])
        
        return res
        