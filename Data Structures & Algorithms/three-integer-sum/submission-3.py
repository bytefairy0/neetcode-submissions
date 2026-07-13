class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        n = len(nums)

        resultSet = set()
        for k in range(n-2):
            p1 = k+1
            p2 = n-1
            while p1 < p2:
                total = nums[p2] + nums[p1] + nums[k]
                if total == 0:
                    resultSet.add((nums[p1], nums[p2], nums[k]))
                    p1 += 1
                    p2 -= 1
                elif total < 0:
                    p1 += 1
                else:
                    p2 -= 1
            
        return [list(item) for item in resultSet]





        