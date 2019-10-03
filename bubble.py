def bubble(A,n):
    for last in range(n,0,-1):
        for num in range(0,last):
            if A[num+1] < A[num]:
                b = A[num]
                A[num] = A[num+1]
                A[num+1] = b
    return A

list = [5,2,1,3]
print(bubble(list,3))