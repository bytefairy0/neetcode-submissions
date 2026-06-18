class Solution:

    def encode(self, strs: List[str]) -> str:
        finalStr = ''
        if not strs:
            return ''
        else:
           for s in strs:
            l = len(s)
            finalStr += f"{l}#{s}"
        return finalStr


    def decode(self, s: str) -> List[str]:
        finalLis = []
        i, j = 0, 0
        while j < len(s):
            if s[j] != '#':
                j += 1
            else:
                l = int(s[i:j])
                finalLis.append(s[j+1: j+l+1])
                i, j = j+l+1, j+l+1
                
        return finalLis
