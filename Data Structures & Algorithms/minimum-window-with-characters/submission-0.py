class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        freqT = {}
        for i in t:
            freqT[i] = 1 + freqT.get(i, 0)

        # track window size and characters
        window = {}
        have, need = 0, len(freqT) 
        res, minL = [-1, -1], float("infinity")

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in freqT and freqT[c] == window[c]:
                have += 1
            
            while have == need:
                if (r-l+1) < minL:
                    minL = r-l+1
                    res = [l, r]

                window[s[l]] -= 1
                if s[l] in freqT and window[s[l]] < freqT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if minL != float("infinity") else ""
                

            