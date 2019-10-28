def quick(A,first, last):
    if first < last :
        p = partition(A,first,last)
        quick(A,first,p-1)
        quick(A,p+1, last)
def partition(A,pivot,last):
    print(A,pivot) #중간확인용
    j = pivot
    i = pivot+1
    while(i <= last):
        if A[i] < A[pivot]:
            j += 1
            if (i != j): 
                a = A[i]
                A[i] = A[j]
                A[j] = a 
        i += 1
    b = A[j]
    A[j] = A[pivot]
    A[pivot] = b
    return j

A = [2,1,5,3,1,6]
quick(A,0,len(A)-1)
print(A)
