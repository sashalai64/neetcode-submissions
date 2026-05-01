class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            l, r = 0, len(s) - 1

            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def backtrack(i, cur):
            if i == len(s):
                res.append(cur[:])
                return
            
            for j in range(i+1, len(s)+1):
                sub = s[i:j]
                if isPalindrome(sub):
                    cur.append(sub)
                    backtrack(j, cur)
                    cur.pop()

        res = []
        backtrack(0, [])

        return res