class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def totalTime(mid):
            total = 0
            for p in piles:
                total += (p - 1) // mid + 1
            return total
        
        l, r = 1, max(piles)
        while l <= r:
            mid = (l + r) // 2
            time = totalTime(mid)

            if time <= h:
                r = mid - 1
            else:
                l = mid + 1
        
        return l