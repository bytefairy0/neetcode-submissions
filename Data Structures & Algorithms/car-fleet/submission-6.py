class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        lis = [(position[i], speed[i]) for i in range(len(position))]
        sortedPos = sorted(lis, reverse=True, key=lambda x: x[0])

        prevMax = None

        fleets = 0
        for i in range(len(position)):
            # floor division round up (a+b-1) // b
            time = (target-sortedPos[i][0])  / sortedPos[i][1]
            if prevMax==None or time > prevMax:
                fleets += 1
                prevMax = time
            
        
        return fleets