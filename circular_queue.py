class CircularQueue:  
    def __init__(self, max_size):
        #최대 크기, queue 생성, 필요한 포인터 초기화
        self.sizee = max_size
        self.front = 0
        self.rear = 0
        self.queue = [None] * self.sizee

    def enqueue(self, data):
        # 원형 큐에 data를 추가
        # 이미 큐가 full인 경우 data추가하지 않고 None을 반환
        # 성공적으로 enqueue한 경우 True반환
        if (self.front - self.rear) == (self.sizee):
            return None
        else:
            b = self.front % self.sizee
            self.queue[b] = data
            self.front += 1
            return True

    def dequeue(self):
        # 큐가 비어 있는 경우 None을 반환
        # 그렇지 않은 경우 data를 반환
        if self.front == self.rear:
            return None
        else:
            c = self.rear % self.sizee
            a = self.queue[c]
            self.queue[c] = None
            self.rear += 1
            return a

    def is_full(self):
        # 큐가 꽉 찼으면 True, 아니면 False
        if (self.front - self.rear) == (self.sizee):
            return True
        else:
            return False

    def is_empty(self):
        # 큐가 비었으면 True, 아니면 False
        if self.front == self.rear:
            return True
        else:
            return False

    def size(self):
        # 현재 큐에 몇 개의 item이 있는지 개수를 반환
        if (self.front - self.rear) == (self.sizee):
            return self.sizee
        else:
            return (self.front-self.rear) % self.sizee

if __name__ == "__main__":
    q = CircularQueue(3)
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print("Enque 10", q.enqueue(10))
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())
    print("Enque 20", q.enqueue(20), q.size())
    print("Enque 30", q.enqueue(30), q.size())
    print("Enque 40", q.enqueue(40), q.size())
    print("Deque", q.dequeue(), q.size())
    print("Enque 50", q.enqueue(50), q.size())
    print("Deque", q.dequeue(), q.size())
    print("Deque", q.dequeue(), q.size())
    print("Enque 60", q.enqueue(60), q.size())
    print("Enque 70", q.enqueue(70), q.size())

    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print("Deque", q.dequeue(), q.size())
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print("Deque", q.dequeue(), q.size())
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print("Deque", q.dequeue(), q.size())
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print("Deque", q.dequeue(), q.size())
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print(len(q.queue)) # should be 4. list 자체의 크기는 변하지 않아야 함

"""
Empty? True , Full? False , Size= 0
Enque 10 True
Empty? False , Full? False , Size= 1
Enque 20 True
Enque 30 True
Enque 40 None
Deque 10
Enque 50 True
Deque 20
Deque 30
Enque 60 True
Enque 70 True
Empty? False , Full? True , Size= 3
Deque 50
Empty? False , Full? False , Size= 2
Deque 60
Empty? False , Full? False , Size= 1
Deque 70
Empty? True , Full? False , Size= 0
Deque None
Empty? True , Full? False , Size= 0
4
"""