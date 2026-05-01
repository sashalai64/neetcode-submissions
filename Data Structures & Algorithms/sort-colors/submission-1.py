class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, k, r = 0, 0, len(nums) - 1

        while k <= r:
            if nums[k] == 0:
                nums[l], nums[k] = nums[k], nums[l]
                l += 1
                k += 1

            elif nums[k] == 2:
                nums[k], nums[r] = nums[r], nums[k]
                r -= 1
            
            else:
                k += 1
        
        return nums