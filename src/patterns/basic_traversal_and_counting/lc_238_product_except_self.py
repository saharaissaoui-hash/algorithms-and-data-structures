#ime Complexity: O(n)
#Space Complexity: O(1) auxiliary (output array not counted)
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Returns an array where each element at index i is the product
        of all elements in nums except nums[i].
        """
        n = len(nums)
        answer = [1] * n

        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]

        right = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer
