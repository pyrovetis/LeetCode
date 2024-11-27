from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        # range starts from 2 so that we can use the loop variable for new row length
        for i in range(2, numRows + 1):
            temp = [0] + result[-1] + [0]
            new_row = []

            for j in range(i):
                new_row.append(temp[j] + temp[j + 1])

            result.append(new_row)

        return result
