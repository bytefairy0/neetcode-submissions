class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        track_count = {}
        for i in nums:
            if track_count.get(i, -1) == 0:
                return True
            else:
                track_count[i] = 0

        return False