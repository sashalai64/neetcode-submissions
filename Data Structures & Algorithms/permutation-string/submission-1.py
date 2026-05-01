class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        win_size = len(s1)
        s1_cnt = [0] * 26
        s2_cnt = [0] * 26
        l = 0

        for s in s1:
            s1_cnt[ord(s) - ord('a')] += 1

        for r in range(len(s2)):
            s2_cnt[ord(s2[r]) - ord('a')] += 1
            if r - l + 1 > win_size:
                s2_cnt[ord(s2[l]) - ord('a')] -= 1
                l += 1

            if s1_cnt == s2_cnt:
                return True
        
        return False