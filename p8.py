# Basic Data Types

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr_list = list(arr)
    smaller = 100
    larger = -101
    
    if n == 1:
        print(arr_list[0])
    else:
        for ct in range(n):
            if larger < arr_list[ct]:
                smaller = larger
                larger = arr_list[ct]
            elif larger > arr_list[ct] and arr_list[ct] > smaller:
                smaller = arr_list[ct]
    
    print(smaller)
    








