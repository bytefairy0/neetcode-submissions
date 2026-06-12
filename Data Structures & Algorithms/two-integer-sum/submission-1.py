class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash of differences
        indices = []
        diff = {}
        for idx in range(len(nums)):
            d = target - nums[idx]
            if d in diff:
                indices = [diff[d], idx]
                return indices
            diff[d] = idx
    
        for idx in range(len(nums)):
            if nums[idx] in diff and diff[nums[idx]] != idx:
                indices.append(idx)
        return indices
