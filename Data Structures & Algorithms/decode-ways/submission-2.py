class Solution:
    def numDecodings(self, s: str) -> int:
        def isValid(sub):
            if 1 <= int(sub) <= 26 and sub[0] != '0':
                return True
            return False

        def dfs(i):
            nonlocal res
            
            if i == n:
                res += 1
                return
            
            for j in range(i, n):
                sub = s[i:j+1]
                if isValid(sub):
                    dfs(j + 1)
                else:
                    return
                
        
        n = len(s)
        res = 0
        dfs(0)

        return res