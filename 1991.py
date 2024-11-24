from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        for index, item in enumerate(nums):
            right -= item
            if left == right:
                return index
            left += item
        return -1
