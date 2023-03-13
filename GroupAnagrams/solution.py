class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
 
        storeChras = ""
        dictIndexStore = {}
        for i in range(len(strs)):
            storeChras = str(sorted(strs[i]))
            if storeChras not in dictIndexStore: 
                dictIndexStore.update({storeChras: [strs[i]]})
            else: 
                dictIndexStore[storeChras].append(strs[i])
        return dictIndexStore.values()
      
    # Another approach 
    def groupAnagramsSecondApproach(self, strs: List[str]) -> List[List[str]]:
    
        mapToString = collections.defaultdict(list)
        for i in strs: 
            count = [0]*26 
            for c in i: 
                count[ord(c) - ord('a')] += 1 
            mapToString[tuple(count)].append(i)
        return mapToString.values()
