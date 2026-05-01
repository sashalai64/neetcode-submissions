class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for n in nums:
            cur = 1
            if n - 1 not in nums:
                while n + cur in nums:
                    cur += 1
            
            res = max(res, cur)
        
        return res

