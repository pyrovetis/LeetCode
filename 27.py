from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0

        for number in nums:
            if number != val:
                nums[counter] = number
                counter += 1

        return counter
