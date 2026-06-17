class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # calculate forward multplication in 
        arr1 = [nums[0]]
        n = len(nums)
        for i in range(1, n):
            arr1.append(arr1[i-1]*nums[i])

        # backward multplication of all numbers
        arr2 = [nums[n-1]]
        for i in range(1, n):
            arr2.append(arr2[i-1]*nums[n-1-i])

        arr2.reverse()
        

        # sliding both arrays:
        final = [arr2[1]]
        for i in range(1, n-1):
            final.append(arr2[i+1]*arr1[i-1])

        final.append(arr1[n-2])

        return final

            



        