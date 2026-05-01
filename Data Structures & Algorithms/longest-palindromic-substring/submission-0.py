class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(l, r):
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            return l + 1, r
        

        res_l, res_r = 0, 0
        for i in range(len(s)):
            even_l, even_r = isPalindrome(i, i + 1)
            odd_l, odd_r = isPalindrome(i, i)

            
            if even_r - even_l > res_r - res_l:
                res_l, res_r = even_l, even_r
            
            if odd_r - odd_l > res_r - res_l:
                res_l, res_r = odd_l, odd_r
        
        return s[res_l:res_r]