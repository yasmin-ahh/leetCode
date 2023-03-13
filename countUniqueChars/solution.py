class Solution:
    def uniqueLetterString(self, s: str) -> int:
        storeIndex = {}
        uniqueChars = set(s)
        newArr = []
        count = 0 
        for i in range(len(s)): 
            if s[i] in uniqueChars and s[i] not in storeIndex: 
                storeIndex.update({s[i]: [-1,i]})
            else: 
                storeIndex[s[i]].append(i)
        for i in storeIndex.keys(): 
            storeIndex[i].append(len(s))
            newArr.append(storeIndex[i])
        for i in newArr: 
            for j in range(1,len(i)): 
                if j+1 <len(i): 
                    count += (i[j]-i[j-1]) * (i[j+1]-i[j])
        return count
