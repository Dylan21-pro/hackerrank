# List Comprehension 


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    small_arr = []
    large_arr = []
    
    
    for l1 in range(x+1):
        for l2 in range(y+1):
            for l3 in range(z+1):
                if (l1 + l2 + l3 != n):
                    small_arr.append(l1)
                    small_arr.append(l2)
                    small_arr.append(l3)
                    large_arr.append(small_arr)
                    small_arr = []
                    
    print(large_arr)
