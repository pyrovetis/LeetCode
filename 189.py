from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cutoff = k % len(nums)
        nums.reverse()
        nums[:cutoff] = reversed(nums[:cutoff])
        nums[cutoff:] = reversed(nums[cutoff:])
