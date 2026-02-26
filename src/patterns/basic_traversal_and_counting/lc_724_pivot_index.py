# Time complexity: O(n)
# Space complexity: O(1)

# Invariant:
# left = sum(nums[:i])
# right = total_sum - left - nums[i]

# Note on enumerate:
# Using `enumerate(nums)` avoids repeated indexing (nums[i])
# and makes the loop both cleaner and slightly more efficient.


from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        Returns the pivot index where the sum of elements strictly
        to the left equals the sum of elements strictly to the right.
        """

        total_sum = sum(nums)
        left = 0

        for i, value in enumerate(nums):
            right = total_sum - left - value

            if left == right:
                return i

            left += value

        return -1
