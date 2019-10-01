def selectionSort(A, n):
    for last in range(n,2,-1):
        for num in range(last,1,-1):
            fir = last
            if A[fir] < A[num]:
                fir = num
            A[fir].change
            print(A[last])
    return A

a = [2,5,3,1]
print(selectionSort(a,3))