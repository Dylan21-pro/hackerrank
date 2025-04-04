# Lists


if __name__ == '__main__':
    N = int(input())
    
    arr = []
    for _ in range(N):
        method = input().split(' ')
        if method[0] == "insert":
            arr.insert(int(method[1]), int(method[2]))
        elif method[0] == "print":
            print(arr)
        elif method[0] == "remove":
            arr.remove(int(method[1]))
        elif method[0] == "append":
            arr.append(int(method[1]))
        elif method[0] == "sort":
            arr.sort()
        elif method[0] == "pop":
            arr.pop()
        elif method[0] == "reverse":
            arr.reverse()






