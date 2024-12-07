from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for i in range(rowIndex):
            next_row = [0 for _ in range(len(row) + 1)]
            for index in range(len(row)):
                next_row[index] += row[index]
                next_row[index + 1] += row[index]

            row = next_row

        return row
