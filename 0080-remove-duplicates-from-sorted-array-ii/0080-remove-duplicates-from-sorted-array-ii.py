class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=0
        k=0
        for i in range(len(nums)):
            if k<2:
                nums[j]=nums[i]
                j+=1
                k+=1
            
            elif nums[i]!=nums[j-2]:
                nums[j]=nums[i]
                j+=1
        return j
