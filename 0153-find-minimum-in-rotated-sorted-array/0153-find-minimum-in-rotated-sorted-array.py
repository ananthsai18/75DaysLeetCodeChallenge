class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        r=n-1
        res=-1
        while(l<=r):
            m=(l+r)//2
            if nums[m]>nums[n-1]:
                l=m+1
            else:
                res=nums[m]
                r=m-1
        return res

        