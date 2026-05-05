from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = defaultdict(int)
        for i in nums:
            seen[i] += 1
        for j in seen.values():
            if j > 1:
                return True
        return False