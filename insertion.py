def insertion(A,n):
    for fir in range(1,n+1):
        for sec in range(0,fir):
            if A[sec] > A[fir]:
                b = A[sec]
                A[sec] = A[fir]
                A[fir] = b
    return(A)

list = [5,2,3,1]
print(insertion(list,len(list)-1))