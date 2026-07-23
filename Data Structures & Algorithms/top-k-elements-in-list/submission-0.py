class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #frequency hashmap
        seen = {}
        for x in nums:
            if x not in seen:
                seen[x] =1
            else:
                seen[x]+=1
        #buckets
        buckets = []
        for n in range(len(nums)+1):
            buckets.append([])
        #fill them
        for num,freq in seen.items():
            buckets[freq].append(num)
        #walk backwards
        final = []
        for freq in range(len(buckets) - 1, -1, -1):
            for num in buckets[freq]:
                final.append(num)
            if len(final) == k:
                return final