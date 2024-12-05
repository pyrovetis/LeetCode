from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        result = 0

        for number in nums:
            if number == 1:
                counter += 1
                result = max(result, counter)
            else:
                counter = 0

        return result
