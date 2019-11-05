def merge_sort(data):
    A = data    
    B = [None]*len(A)                #정렬한 결과를 담을 빈 배열을 만든다.
    mergeSort(A,B,0,len(A)-1)
    data = B
    return data
def mergeSort(A,B,first,last):
    if first < last :                #first와 last가 같을 때까지 반복한다.
        mid = (first+last)//2
        mergeSort(A,B,first,mid)
        mergeSort(A,B,mid+1,last)
        merge(A,B,first,mid,last)
        
def merge(A,B,first, mid, last):
    i = first
    j = mid+1
    k = first
    while i <= mid and j <= last:
        if (A[i] <= A[j]):          #두 배열에서 작은 것을 찾아 B에 넣어준다.
                B[k] = A[i]
                i += 1
        else:
                B[k] = A[j]
                j += 1
        k += 1
    if(i > mid):                    #한 배열이 모두 B에 들어갔다면 남은 배열도 B에 넣어준다.
        while(j <= last):
                B[k] = A[j]
                k += 1
                j += 1
    else:
        while(i <= mid):
                B[k] = A[i]
                k += 1
                i += 1
    for k in range(first, last+1):  #B를 A에 넣어준다.
            A[k] = B[k] 