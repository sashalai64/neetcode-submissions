class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        res = 0
        cache = {}

        def isValid(sub):
            if 1 <= int(sub) <= 26 and sub[0] != '0':
                return True
            return False

        def dfs(i):            
            if i == n:
                return 1
            
            if i in cache:
                return cache[i]
            
            ways = 0
            for j in range(i, n):
                sub = s[i:j+1]
                if isValid(sub):
                    ways += dfs(j + 1)
                else:
                    break
            
            cache[i] = ways
            return ways

       
        return dfs(0)
