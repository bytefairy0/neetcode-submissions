class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Brute force approch
        n = len(piles)
        upperBound = max(piles)

        l, r = 1, upperBound

        while l <= r:
            curr_rate = l + (r - l) // 2
            sum_rates = 0
            for i in range(n):
                sum_rates += (piles[i] + curr_rate - 1) // curr_rate
            if sum_rates <= h:
                r = curr_rate - 1
            else:
                l = curr_rate + 1

        return l
        

