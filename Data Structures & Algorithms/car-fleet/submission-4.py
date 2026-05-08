class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        res = 0

        for i in range(n):
            position[i] = [position[i], (target - position[i]) / speed[i]]

        position.sort(reverse = True)    
        
        arriveTime = -float('inf')
        for i in range(n):
            if position[i][1] > arriveTime:
                res += 1
                arriveTime = position[i][1]
        
        return res