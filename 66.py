from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = int("".join(map(str, digits)))
        result += 1
        return [int(x) for x in str(result)]
