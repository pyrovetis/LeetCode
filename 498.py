from collections import defaultdict
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        temp_dictionary = defaultdict(list)
        result = []

        for row in range(rows):
            for col in range(cols):
                index = row + col
                item = mat[row][col]
                temp_dictionary[index].append(item)

        for key, value in temp_dictionary.items():
            if key % 2:
                result += value
            else:
                result += value[::-1]

        return result
