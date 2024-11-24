from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums, reverse=True)
        if sorted_nums[0] >= sorted_nums[1] * 2:
            return nums.index(sorted_nums[0])

        return -1
