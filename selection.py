def selectionSort(A, n):
    for last in range(n,0,-1):
        max = last
        b = A[last]
        for num in range(last-1,-1,-1):
            if A[num] > A[max]:
                max = num
<<<<<<< HEAD
        A[last] = A[max]        
        A[max] = b        
    return A

a = [2,5,3,1]
print(selectionSort(a,len(a)-1))
=======
        A[last] = A[max]
        A[max] = b
    return A

a = [2,5,3,1]
print(selectionSort(a,3))
>>>>>>> cd0d12645ba7cb359284fb480b4c436331bfeed1
