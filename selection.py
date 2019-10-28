def selectionSort(A, n):
    for last in range(n,0,-1):
        max = last
        b = A[last]
        for num in range(last-1,-1,-1):
            if A[num] > A[max]:
                max = num
        A[last] = A[max]        
        A[max] = b        
    return A

a = [2,5,3,1]
print(selectionSort(a,len(a)-1))