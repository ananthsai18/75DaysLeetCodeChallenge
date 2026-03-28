class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(mid):
            count = 1
            curr = 0

            for num in nums:
                if curr + num <= mid:
                    curr += num
                else:
                    count += 1
                    curr = num

            return count

        left = max(nums)
        right = sum(nums)
        res = right

        while left <= right:
            mid = (left + right) // 2
            parts = canSplit(mid)
            if parts <= k:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res
        