def selection_sort(data):
    n = len(data)-1
    for last in range(n,0,-1):          #last에 뒤에서부터 하나씩 넣어준다.
        max = last              
        b = data[last]      
        for num in range(last-1,-1,-1): #num에 last의 앞에서부터 하나씩 넣어준다.
            if data[num] > data[max]:   #가장 큰 값과 가장 마지막 값을 교환해준다.
                max = num
            data[last] = data[max]        
        data[max] = b        
    return data