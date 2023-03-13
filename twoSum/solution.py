class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      
        storeI1 = -1 
        for i in range(0,len(nums)): 
            value = target - nums[i]
            if value in nums and i != nums.index(value) : 
                return i,nums.index(value)
                break 
