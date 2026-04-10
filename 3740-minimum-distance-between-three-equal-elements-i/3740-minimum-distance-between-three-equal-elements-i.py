class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n=len(nums)
        t=float("inf")
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]==nums[j] and nums[j] ==nums[k]:
                        k=abs(i-j)+abs(j-k)+abs(k-i)
                        t=min(t,k)
        if t==float("inf"):
            return -1
        return t

