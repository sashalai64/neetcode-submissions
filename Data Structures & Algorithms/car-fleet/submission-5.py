class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        res = 1

        for i in range(n):
            position[i] = [position[i], (target - position[i]) / speed[i]]

        position.sort(reverse = True)    
        
        arriveTime = position[0][1]
        for i in range(1, n):
            if position[i][1] > arriveTime:
                res += 1
                arriveTime = position[i][1]
        
        return res