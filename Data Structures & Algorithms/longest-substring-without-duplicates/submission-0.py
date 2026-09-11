class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashTable = {}
        maxLen = 0
        l = 0

        for r in range(len(s)):
            if s[r] in hashTable:
                l = max(hashTable[s[r]]+1, l)
            hashTable[s[r]] = r
            maxLen = max(r-l+1, maxLen)

        return maxLen
