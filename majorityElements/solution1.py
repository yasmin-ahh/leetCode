class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapCount = {}
        for i in nums: 
            if i not in mapCount: 
                mapCount.update({i: 0})
            else: 
                mapCount[i] += 1 
        maxVal = max(mapCount.values())
        
        for i,j in enumerate(mapCount): 
            print(mapCount[j])
            if  mapCount[j] >= floor(len(nums)/2): 
                return j
