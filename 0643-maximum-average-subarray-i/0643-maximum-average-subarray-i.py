class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg=0
        n=len(nums)
        i=0
        j=0
        ans=float("-inf")
        while(j<n):
            avg+=nums[j]
            if j-i+1 > k:
                avg-=nums[i]
                i+=1

            if j-i+1 == k:
                ans=max(ans,(avg/k))
            j+=1
        return ans
        