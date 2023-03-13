class Solution:
  
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      
        listNums = [str(i) for i in range(1,10)]
        countOflistNums = 0 
        indices = [(x % 3, int(x / 3)) for x in range(0, 9)]
        boxes = [[board[x*3+xx][y*3+yy] for xx, yy in indices] for x, y in indices]
        boolCheck = True
        
        for i in range(len(board)): 
            for m in range(len(listNums)): 
                if (board[i].count(listNums[m])>1) or ([jm[i] for jm in board].count(listNums[m]))>1 or (boxes[i].count(listNums[m])>1): 
                    boolCheck = False 
                    break 

        return boolCheck 
