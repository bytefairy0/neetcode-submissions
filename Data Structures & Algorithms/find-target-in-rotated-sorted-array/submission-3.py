class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0: 
            return -1

        st, end = 0, n-1
        while st < end:
            mid = st + (end-st)//2
            
            if nums[mid] == target:
                return mid
            
            # right half sorted
            if nums[mid] < nums[end]:
                if nums[mid] < target <= nums[end]:
                    st = mid+1
                else:
                    end = mid-1
            
            # left half sorted
            else: 
                if nums[st] <= target < nums[mid]:
                    end = mid-1
                else:
                    st = mid+1

        return st if nums[st] == target else -1 # to check wen st==end


            

