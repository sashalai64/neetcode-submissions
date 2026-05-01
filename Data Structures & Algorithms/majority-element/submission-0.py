class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        maxFreq = 0
        res = 0

        for n in nums:
            freq[n] += 1
            if freq[n] > maxFreq:
                maxFreq = freq[n]
                res = n

        return res 