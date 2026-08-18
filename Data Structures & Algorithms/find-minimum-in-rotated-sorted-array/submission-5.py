class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1

        while l < r:
            mid = l + (r-l)//2

            if nums[mid] > nums[r]: # mid and r are in same sorted segment, threw away right half
                l = mid + 1
            else:
                r = mid 
            
        return nums[l]