class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        # store the sorted words as keys and their words (same) as keys of list
        for s in strs:
            sortedStr = " ".join(sorted(s))
            if sortedStr in dic:
                dic[sortedStr].append(s)
            else:
                dic[sortedStr] = [s]
            
        finalLis = []
        for key, val in dic.items():
            finalLis.append(val)
       
        return finalLis
