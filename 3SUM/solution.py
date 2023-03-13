class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        newe_set = set()
        nums.sort()
        for i in range(len(nums)): 
            x = nums[i]
            low = i +1 
            high = len(nums) - 1 

            while low < high: 
                if x + nums[low] +nums[high] == 0: 
                    newe_set.add(tuple(sorted([x,nums[low],nums[high]])))
                    low = low +1 
                    high = high -1
                elif  x + nums[low] +nums[high] <0: 
                    low += 1 
                elif x + nums[low] +nums[high] >0: 
                    high -= 1 
        return newe_set
