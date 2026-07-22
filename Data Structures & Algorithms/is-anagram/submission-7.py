class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #    return False
        #for x in set(s):
        #    if s.count(x) != t.count(x):
        #        return False
        #return True

        mapS = {}
        mapT = {}
        for c in s:
            mapS[c] = mapS.get(c,0)+1
        for c in t:
            mapT[c] = mapT.get(c,0)+1
        if mapT == mapS:
            return True
        return False    