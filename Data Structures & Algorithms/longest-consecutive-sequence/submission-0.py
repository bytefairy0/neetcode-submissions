class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashSet = set(nums)
        seqTable = {}
        for i in nums:
            if i-1 not in hashSet:
                seqTable[i-1] = 0
                # now we have possible starts of sequences
        
        maxCount = 0
        for key in seqTable.keys():
            curr = key
            while curr+1 in hashSet:
                seqTable[key] += 1
                curr = curr+1
            if maxCount < seqTable[key]:
                maxCount = seqTable[key]

        return maxCount

                

