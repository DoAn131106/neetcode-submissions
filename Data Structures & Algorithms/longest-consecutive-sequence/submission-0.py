class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        distinct = set(nums)
        best = 0
        for i in distinct:
            if (i - 1) not in distinct:
                lengthsofar = 1
                while i + lengthsofar in distinct:
                    lengthsofar += 1
                best = max(best, lengthsofar)
        return best