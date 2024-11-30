from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        for characters in zip(*strs):
            # if there is more than one unique character in this position across all strings, break the loop
            if len(set(characters)) > 1:
                break

            # all characters in this position are the same, add it to the result
            result += characters[0]

        return result
