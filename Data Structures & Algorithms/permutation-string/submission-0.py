class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)

        for c in s1:
            freq1[c] += 1
        
        i, j = 0, 0
        while j < len(s2):
            freq2[s2[j]] += 1

            if j - i + 1 == len(s1):
                if freq1 == freq2:
                    return True

                freq2[s2[i]] -= 1
                if freq2[s2[i]] == 0:
                    del freq2[s2[i]]
                i += 1
            j += 1
        
        return False