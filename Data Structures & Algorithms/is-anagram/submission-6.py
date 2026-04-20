class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = defaultdict(int)
        count = Counter(s)

        for c in t:
            if c not in count or count[c] == 0:
                return False
            freq[c] += 1
        
        return freq == count
        
