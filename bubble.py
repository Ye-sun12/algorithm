def bubble_sort(data):
    n = len(data)-1
    for fir in range(1,n+1):            #fir에 1번부터 끝까지 넣어준다.
        for sec in range(0,fir):        #sec에 0번부터 fir까지 넣어준다.
            if data[sec] > data[fir]:   #만약 sec가 fir보다 크면 둘의 자리를 바꿔준다.
                b = data[sec]
                data[sec] = data[fir]
                data[fir] = b
    return data