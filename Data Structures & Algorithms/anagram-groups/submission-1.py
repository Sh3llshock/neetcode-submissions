

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we make a hashmap that has values list
        groups = defaultdict(list)
        #for each word we wanna see whats its abcList
        for w in strs:
            abcList = [0]*26
            for c in w:
                index = ord(c)-ord("a")
                abcList[index]+=1
                
            key=tuple(abcList)
            groups[key].append(w)
            
        return list(groups.values())