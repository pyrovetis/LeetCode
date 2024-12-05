from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        result = float("inf")

        for right, _ in enumerate(nums):
            total += nums[right]
            while total >= target:
                result = min(right - left + 1, result)
                total -= nums[left]
                left += 1

        if result == float("inf"):
            return 0

        return result
