from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        while matrix:
            # pop top row and append to result
            result.extend(matrix.pop(0))
            # rotate matrix
            matrix = list(zip(*matrix))[::-1]

        return result
