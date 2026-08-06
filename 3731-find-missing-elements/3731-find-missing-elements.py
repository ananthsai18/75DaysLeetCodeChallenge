class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        p=set(nums)
        arr=[]
        for i in range(nums[0],nums[-1]):
            if i not in p:
                arr.append(i)
        return arr 