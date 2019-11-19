class SinglyLinkedList:
    class Node:
        def __init__(self, value):
            self.next = None
            self.value = value
    
    def __init__(self):
        self.head = None

    def insert_head(self, value):
        if (self.head == None):
            self.head = self.Node(value)
        else:
            a = self.Node(value)
            a.next = self.head
            self.head = a
    
    def insert_tail(self, value):
        if (self.head == None):
            self.head = self.Node(value)
        else:
            a = self.Node(value)
            p = self.head
            b = None
            while (p):
                b = p
                p = p.next
            b.next = a

    def delete_head(self):
        a = self.head.value
        self.head = self.head.next
        return a

list = SinglyLinkedList()
list.insert_head(5)
list.insert_head(10)
list.insert_head(3)
v = list.delete_head()
print(v) #3

list.insert_tail(7)
list.insert_tail(2)

p = list.head
while p:
    print(p.value, end = " ")
    p = p.next # 한 바퀴 돔
print()
    # 출력 결과 : 10 5