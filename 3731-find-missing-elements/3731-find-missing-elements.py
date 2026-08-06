class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr=[]
        for i in range(nums[0],nums[-1]):
            if i not in nums:
                arr.append(i)
        return arr 