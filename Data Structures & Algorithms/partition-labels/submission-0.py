class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        last = {}
        count = 0
        last_max = 0

        for i in range(len(s)):
            last[s[i]] = i

        for i in range(len(s)):
            last_max = max(last_max, last[s[i]])
            count += 1

            if last_max == i:
                res.append(count)
                count = 0
        
        return res