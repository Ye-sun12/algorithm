class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None
        def __str__(self):
            return f"NODE[{self.value}]"

    def __init__(self):
        self.head = self.Node(None)
        self.head.next = self.head
        self.head.prev = self.head
        self.size = 0

    def is_empty(self):
    #비었으면 True, 아니면 False
        if (self.size == 0):
            return True
        else:
            return False

    def add_after(self, node, value):
        a = self.Node(value)        #새로운 노드를 만든다.
        a.next = node.next          #새로 만든 노드와 기존의 노드를 연결한다.
        node.next.prev = a
        node.next = a
        a.prev = node
        self.size += 1              #노드가 하나 추가되었기 때문에 크기에 1을 더한다.

    def add_before(self, node, value):
        a = self.Node(value)        #새로운 노드를 만든다.
        node.prev.next = a          #새로 만든 노드와 기존의 노드를 연결한다.
        a.prev = node.prev
        node.prev = a
        a.next = node
        self.size += 1              #노드가 하나 추가되었기 때문에 크기에 1을 더한다.

    def add_head(self, value):
        #add_after 활용
        a = self.Node(value)        #노드를 하나 만든다.
        if self.size == 0:          #만약 크기가 0이라면 head의 next와
            self.head.next = a      #head의 prev를 새로 만든 노드와 연결한다.
            a.prev = self.head
            self.head.prev = a
            a.next = self.head
        else:
            self.head.next.prev = a #head의 next와 새로 만든 노드를 연결한다.
            a.next = self.head.next
            self.head.next = a
            a.prev = self.head
        self.size += 1              #노드가 하나 추가되었기 때문에 크기에 1을 더한다.

    def add_tail(self, value):
        #add_before 활용
        a = self.Node(value)        #노드를 하나 만든다.
        if self.size == 0:          #만약 크기가 0이라면 head의 next와
            self.head.next = a      #head의 prev를 새로 만든 노드와 연결한다.
            a.prev = self.head
            self.head.prev = a
            a.next = self.head
        else:
            a.prev = self.head.prev #head의 prev를 새로 만든 노드로 바꾼다.
            self.head.prev.next = a
            self.head.prev = a
            a.next = self.head
        self.size += 1              #노드가 하나 추가되었기 때문에 크기에 1을 더한다.

    def remove(self, node):
        node.next.prev = node.prev  #삭제할 노드의 prev와 next를 서로 연결한다.
        node.prev.next = node.next
        self.size -= 1              #노드가 하나 삭제되었기 때문에 크기에 1을 뺀다.

    def remove_head(self):
        #empty인지 아닌지 검사하여 제거
        if self.size == 0:                
            print("remove할 수 없습니다.")
        else:
            self.head.next = self.head.next.next #head의 next와 head의 next의 next를 연결한다.
            self.head.next.prev = self.head
            self.size -= 1                       #노드가 하나 삭제되었기 때문에 크기에 1을 뺀다.

    def remove_tail(self):
        #empty인지 아닌지 검사하여 제거
        if self.size == 0:
            print("remove할 수 없습니다.")
        else:
            self.head.prev = self.head.prev.prev #head의 prev와 head의 prev의 prev를 연결한다.
            self.head.prev.next = self.head
            self.size -= 1                       #노드가 하나 삭제되었기 때문에 크기에 1을 뺀다.

    def traverse(self, dir = 1):
        # generator를 이용하여 리스트를 정방향(dir=1) 혹은 역방향(dir=-1)으로 순회할 수 있도록 함
        node = self.head.next if dir == 1 else self.head.prev
        while node != self.head:
            yield node
            node = node.next if dir == 1 else node.prev

    def find(self, value, from_node = None):
        #검색하기
        if from_node == None:       #from_node에 아무것도 들어오지 않았다면 
            from_node = self.head   #from_node에 헤드를 넣어 처음부터 검사해준다.
        node = from_node.next   
        while node != self.head:    
            if node.value == value: #node를 찾으면 node를 반환한다.
                return node
            node = node.next
        return None                 #못 찾으면 None을 반환한다.

    def print(self, dir = 1):
        print("FORWARD: " if dir==1 else "BACKWARD:", end = "")
        for node in self.traverse(dir):
            print(node.value, end="->")
        print()

if __name__ == "__main__":
    list = LinkedList()
    list.print()
    list.print(-1)
    print("IS_EMPTY?", list.is_empty())
    list.add_head(1)
    list.add_head(3)
    list.add_tail(3)
    list.add_tail(4)
    list.print()
    list.print(-1)
    print("IS_EMPTY?", list.is_empty())

    a = list.find(3)
    print(a)
    b = list.find(3, from_node=a)
    print(b)
    list.add_before(b, 9)
    list.add_after(b, 5)

    list.print()
    list.print(-1)

    c = list.find(4)
    list.remove(c)

    list.print()
    list.print(-1)

    list.remove_head()
    list.remove_head()

    list.print()
    list.print(-1)

    list.remove_tail()
    list.remove_tail()

    list.print()
    list.print(-1)
    print("IS_EMPTY?", list.is_empty())

    list.remove_head()
    list.print()
    print("IS_EMPTY?", list.is_empty())

"""
FORWARD:
BACKWARD:
IS_EMPTY? True
FORWARD: 3->1->3->4->
BACKWARD: 4->3->1->3->
IS_EMPTY? False
NODE[3]
NODE[3]
FORWARD: 3->1->9->3->5->4->
BACKWARD: 4->5->3->9->1->3->
FORWARD: 3->1->9->3->5->
BACKWARD: 5->3->9->1->3->
FORWARD: 9->3->5->
BACKWARD: 5->3->9->
FORWARD: 9->
BACKWARD: 9->
IS_EMPTY? False
FORWARD:
IS_EMPTY? True
"""