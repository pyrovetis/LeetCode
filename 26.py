from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 1

        for index in range(1, len(nums)):
            if nums[index] != nums[index - 1]:
                nums[counter] = nums[index]
                counter += 1

        return counter
