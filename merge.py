def mergeSort(A,B,first,last):
    if first < last :
        mid = (first+last)//2
        mergeSort(A,B,first,mid)
        mergeSort(A,B,mid+1,last)
        merge(A,B,first,mid,last)
        
def merge(A,B,first, mid, last):
    i = first
    j = mid+1
    k = first
    while i <= mid and j <= last:
        if (A[i] <= A[j]):
                B[k] = A[i]
                i += 1
        else:
                B[k] = A[j]
                j += 1
        k += 1
    if(i > mid):
        while(j <= last):
                B[k] = A[j]
                k += 1
                j += 1
    else:
        while(i <= mid):
                B[k] = A[i]
                k += 1
                i += 1
    for k in range(first, last+1):
            A[k] = B[k] 
A = [2,5,3,1]
B = [None]*len(A)
mergeSort(A,B,0,len(A)-1)
print(A)
