# Time complexity: O(n)
# Space complexity: O(1)

# Given n and a list of n-1 distinct numbers from 1..n,
# return the missing number.
# Uses the arithmetic sum formula:
# 1 + 2 + ... + n = n * (n + 1) // 2

import sys 

def main() -> None: 
    data = sys.stdin.read().split()

    n = int(data[0]) 
    nums = list(map(int, data[1:]))

    expected = n * (n+1) // 2
    actual = sum(nums)

    print(expected - actual)

if __name__ == "__main__": 
    main()