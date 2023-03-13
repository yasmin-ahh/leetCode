class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        startList1 = []
        startList2 = []
        for v in s: 
            if v != "#": 
                startList1.append(v)
            elif v == "#" and len(startList1) >0: 
                del startList1[len(startList1)-1]
        for v in t: 
            if v != "#": 
                startList2.append(v)
            elif v == "#" and len(startList2) >0: 
                del startList2[len(startList2)-1]
        if str(startList1) == str(startList2): 
            return True 
        else: 
            return False
