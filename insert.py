def insertion_sort(data):
    n = len(data)
    for fir in range(1,n):              #fir에 1번부터 끝의 하나 전까지 넣어준다.
        for sec in range(fir,0,-1):     #sec에 fir부터 1번까지 넣어준다.
            if data[sec-1] > data[sec]: #만약 앞이 뒤에 보다 크면 둘의 자리를 바꿔준다.
                a = data[sec]           #그러면서 fir의 자리를 찾아준다.
                data[sec] = data[sec-1]
                data[sec-1] = a
    return data                         #정렬이 끝나면 data를 리턴한다.