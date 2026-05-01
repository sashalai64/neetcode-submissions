class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMap = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        def dfs(i, cur):
            if i == n:
                res.append(cur)
                return
            
            for char in digitMap[digits[i]]:
                dfs(i + 1, cur + char)


        n = len(digits)
        if n == 0:
            return []

        res = []
        dfs(0, '')

        return res