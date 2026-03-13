class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums=sorted(nums)
        n=len(nums)
        for i in range(n-1):
            if nums[i+1]==nums[i]:
                return True
        return False
        