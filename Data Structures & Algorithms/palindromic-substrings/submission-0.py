class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalindrom(l, r):
            cnt = 0
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                cnt += 1
                l -= 1
                r += 1
            return cnt

        res = 0
        for i in range(len(s)):
            odd = isPalindrom(i, i)
            even = isPalindrom(i, i + 1)
            res += odd + even
        
        return res