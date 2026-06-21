class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()
        # two pointer approach
        l = len(s)
        for i in range(l):
            if s[i] != s[l-1-i]:
                return False

        return True