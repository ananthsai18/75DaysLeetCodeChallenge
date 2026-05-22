class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        if len(nums)==1:
            return 0
        l=0
        if nums[0]>nums[1]:
            return 0
        if nums[n-1]>nums[n-2]:
            return n-1
       
        h=n-1
        
        while(l<h):
            m=(l+h)//2
            if nums[m]<nums[m+1]:
                l=m+1
            else:
                h=m
        return l
        