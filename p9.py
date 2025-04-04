# Nested lists

if __name__ == '__main__':
    name_list = []
    score_list = [] 
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_list.append(name)
        score_list.append(score)
            
    smaller = 1000.0
    larger = -1000.0
    
    
    if len(name_list) == 1:
        print(name_list[0])
    else:
        for ct in range(len(score_list)):
            if smaller > score_list[ct]:
                larger = smaller
                smaller = score_list[ct]
            elif smaller < score_list[ct] and score_list[ct] < larger:
                larger = score_list[ct]
        
            
    indices = [i for i, x in enumerate(score_list) if x == larger]
    
    arr = []
    
    for ct in indices:
        arr.append(name_list[ct])
        
    arr_sorted = sorted(arr)
    
    for arg in arr_sorted:
        print(arg)
    
    
    




