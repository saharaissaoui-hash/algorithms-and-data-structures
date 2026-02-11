# Time complexity: O(n)
# Space complexity: O(n)

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """
        Computes the running sum of the array.
        result[i] = nums[0] + ... + nums[i]
        """

        n = len(nums)
        if n == 0:
            return []

        # We allocate a new array of size n.
        # Using [nums[0]] * n would replicate the same reference.
        # That is safe for integers (immutable), but dangerous for mutable types.
        # Example:
        # arr = [[0]] * 3
        # arr[0][0] = 5  →  [[5], [5], [5]]
        # because all entries reference the same object.
        # Using [0] * n clearly communicates independent positions.
        result = [0] * n

        result[0] = nums[0]

        for i in range(1, n):
            result[i] = result[i - 1] + nums[i]

        return result
