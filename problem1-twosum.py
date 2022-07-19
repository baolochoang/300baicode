class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Create the dictionary
        hashMap = {}
        
        for i in range (len(nums)):
            num = nums[i]
            if (target - num) in hashMap:
                return [hashMap[target - num], i]
            
            hashMap[num] = i
