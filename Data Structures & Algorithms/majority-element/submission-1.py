class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1
        
        res = 0
        maxVal = -1

        for key, val in freq.items():
            if val > maxVal:
                res = key
                maxVal = val
        
        return res