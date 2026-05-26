class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        b=set(nums2)
        nums1.sort()
        for i in nums1:
            if i in b:
                return i
        return -1
        