import sys 

def main()-> None: 

    data = sys.stdin.readline().strip()
    n = len(data)

    if n == 0:
        print(0)
        return
    
    curr_length, max_length = 1, 1
    slow = 0

    for c in data[1:]: 
        if c == data[slow]: 
            curr_length += 1 
        else : 
            slow += curr_length
            curr_length = 1
        max_length = max(max_length, curr_length)

    print(max_length) 


if __name__ == "__main__": 
    main()