import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums 
        self.nums2 = list(nums)
    def reset(self) -> List[int]:
        self.nums = self.nums2
        self.nums2 = list(self.nums2)
        return self.nums 

    def shuffle(self) -> List[int]:
        shif_list = []
        for i in range(len(self.nums)):
            randIndex = random.randrange(len(self.nums))
            shif_list.append(self.nums[randIndex])
            self.nums.pop(randIndex)
        self.nums = shif_list
        return self.nums
