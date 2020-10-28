class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        newnums = []
       
        for i,e in enumerate(nums):
            if i < n:
                newnums.append(e)
            
                newnums.append(nums[i+n])
        return newnums;
