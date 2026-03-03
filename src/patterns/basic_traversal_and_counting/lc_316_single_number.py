from typing import List

def singleNumber(nums: List[int]) -> int:
    return 2*sum(set(nums)) - sum(nums)
    
## another solution XOR: 
## a ^ a = 0 
## a ^ 0 = a

def singleNumber(nums: List[int]) -> int:
    result = 0
    for n in nums:
        result ^= n
    return result