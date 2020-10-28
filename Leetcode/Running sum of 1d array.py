class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        newnums = nums.copy()
        for i in range(len(nums)):
            newnums[i] = sum(nums[:(i+1)])
               
        return newnums;
