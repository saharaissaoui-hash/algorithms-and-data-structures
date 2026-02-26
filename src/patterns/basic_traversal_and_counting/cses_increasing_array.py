# Time complexity: O(n)
# Aux space complexity: O(1)

import sys 

def main() -> None: 
    
    data = sys.stdin.read().split()
    n = int(data[0])
    nums = list(map(int, data[1:]))

    moves, curr_max = 0, nums[0]
    for i in range(1, n):
        if nums[i] < curr_max: 
            moves += curr_max - nums[i]
        else: 
            curr_max = nums[i]

    print(moves)


if __name__ == "__main__": 
    main()