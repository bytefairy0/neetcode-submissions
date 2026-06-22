class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers
        n = len(numbers)
        p1 = 0
        p2 = n-1

        for i in range(n):
            # create index bounds
            sum = numbers[p1] + numbers[p2]
            if sum == target:
                return [p1+1, p2+1]
            elif sum < target:
                p1 += 1
            else:
                p2 -= 1
            
        return None
                
        