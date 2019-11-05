def quick_sort(data):
    quickSort(data,0,len(data)-1)    #quickSort함수를 불러온다.
    return data
def quickSort(A,first, last):                      
    if first < last :                #first와 last가 같을 때까지 quickSort를 불러온다.
        p = partition(A,first,last)         
        quickSort(A,first,p-1)
        quickSort(A,p+1, last)
def partition(A,pivot,last):         #가장 앞의 있는 것을 pivot으로 설정한다.
    j = pivot                    
    i = pivot+1                      
    while(i <= last):                #A[i]가 A[pivot]보다 크면 i와 j를 하나씩 증가한다.
        if A[i] < A[pivot]:          #A[i]가 A[pivot]보다 작으면 j를 하나씩 증가하고
            j += 1                    #A[i]와 A[j]를 바꾼다.
            if (i != j): 
                a = A[i]
                A[i] = A[j]
                A[j] = a 
        i += 1
    b = A[j]                        #last까지 비교가 끝나면 A[j]와 A[pivot]을 교환한다.
    A[j] = A[pivot]
    A[pivot] = b
    return j