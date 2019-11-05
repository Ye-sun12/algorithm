def heap_sort(data):                    
    n = len(data)-1
    for i in range((n//2)+1,-1,-1):     #최초힙을 만들어준다.
        heap(data,i,n) 
    for i in range(n):                  #가장 뒤에 있는 것과 가장 앞에 있는 것을 교환하며 정렬해준다.
        b = data[0]                    
        data[0] = data[n]
        data[n] = b
        heap(data,0,n-1)                #교환한 후 다시 힙으로 만들어 준다.
        n -= 1
    return data                         #정렬이 끝나면 data를 리턴해준다.
def heap(A,i,size):
    while 2*i+1<= size:                 
        k = 2*i+1                       #k는 자식 중에 왼쪽에 있는 것이다.
        if k < size and A[k] < A[k+1]:  
            k += 1
        if A[i] >= A[k]:                #부모가 자식보다 더 크면 while문을 벗어난다.
            break
        b = A[i]                        #자식이 부모보다 크면 위치를 바꾼다.
        A[i] = A[k]
        A[k] = b
        i = k