class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create n buckers
        freq = [[] for _ in range(0, len(nums))]
        for i in nums:
            idx = i % len(nums)
            freq[idx].append(i)
        
        # sort based on length
        freq.sort(key=len, reverse=True)
        print(freq)

        arr = []
        for i in range(0, k):
            if freq[i]:
                arr.append(freq[i][0])

        return arr