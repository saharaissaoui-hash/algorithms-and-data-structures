#time Complexity: O(n)
#Space Complexity: O(1)
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        curr = nums[0]

        for x in nums[1:]:
            curr = max(x, curr + x)
            best = max(best, curr)

        return best