class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, k, r = 0, 0, len(nums) - 1

        while k <= r:
            if nums[k] == 0:
                nums[l], nums[k] = nums[k], nums[l]
                k += 1
                l += 1
            
            elif nums[k] == 1:
                k += 1
            
            else:
                nums[k], nums[r] = nums[r], nums[k]
                r -= 1