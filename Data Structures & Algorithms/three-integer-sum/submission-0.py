class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        l, k, r = 0, 0, n - 1
        res = set()

        while l < n - 2:
            k = l + 1
            r = n - 1
            while k < r:
                if nums[l] + nums[k] + nums[r] == 0:
                    res.add((nums[l], nums[k], nums[r]))
                    k += 1
                    r -= 1
                
                elif nums[l] + nums[k] + nums[r] < 0:
                    k += 1
                
                else:
                    r -= 1
            l += 1
        
        return list(res)