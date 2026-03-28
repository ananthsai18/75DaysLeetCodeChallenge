class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        if len(nums)==1:
            return nums[0]
        l=1
        r=n-2
        while(l<=r):
            m=(l+r)//2
            if nums[0] != nums[1]: 
                return nums[0]
            if nums[n-1] != nums[n-2]: 
                return nums[n-1]
            if nums[m-1]!=nums[m] and nums[m+1]!=nums[m]:
                return nums[m]
            elif nums[m+1]==nums[m]:
                if m%2==0:
                    l=m+1
                else:
                    r=m-1
            elif nums[m-1]==nums[m]:
                if (m-1)%2==0:
                    l=m+1
                else:
                    r=m-1
        return -1
            