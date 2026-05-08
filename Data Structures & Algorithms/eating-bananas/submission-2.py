class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def totalTime(speed):
            time = 0
            for p in piles:
                time += math.ceil(p / speed)
            
            return time
            
        l, r = 1, max(piles)
        
        while l <= r:
            mid = (l + r) // 2
            time = totalTime(mid)

            # left most valid ans
            if time <= h:
                r = mid - 1
            else:
                l = mid + 1
        
        return l