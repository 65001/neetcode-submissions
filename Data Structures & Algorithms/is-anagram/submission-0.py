class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}
        for c in s:
            temp = sDict.get(c)
            if temp is None:
                sDict[c] = 1
            else:
                sDict[c] += 1
        for c in t:
            temp = tDict.get(c)
            if temp is None:
                tDict[c] = 1
            else:
                tDict[c] += 1
        return sDict == tDict