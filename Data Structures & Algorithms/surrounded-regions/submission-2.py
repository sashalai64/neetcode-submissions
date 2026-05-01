class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return
            
            board[i][j] = 'Y'
            
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        m = len(board)
        n = len(board[0])

        # Find all O that are connected to the border
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    dfs(i, j)
        
        # Convert the rest of the O to X
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        
        # Convert the all O connected to the border back to O
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'Y':
                    board[i][j] = 'O'