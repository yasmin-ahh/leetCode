class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        arr = []
        
        for i in range(k): 
            check1 = nums[(len(nums))-1]
            del nums[(len(nums))-1]
            nums.insert(0, check1)
