class CLList:
    #노드만들기 위해 클래스 안에 클래스
    class Node:
        def __init__(self, name, link):
            self.name = name
            self.link = link

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def size(self):
        return self.size

    def isEmpty(self): #비어있으면 삭제 불가
        return self.size == 0 #0이면 True 아니면 False

    def insertFront(self, name):
        if self.isEmpty(): #노드가 1개면 head이자 tail
            t = self.Node(name, None)
            self.head = t
            self.head.link = t
            self.tail = t
        else:
            self.head = self.Node(name, self.head)
            self.tail.link = self.head
        self.size += 1

    def insertRear(self, name, p): #name을 p다음에 삽입
        if p == None:
            self.insertFront(name)
        elif p != self.tail: #삽입위치가 있다. 제일 마지막에 수행되는 부분
            p.link = CLList.Node(name, p.link)
        else: #tail인경우
            t = CLList.Node(name, self.head)
            self.tail.link = t
            self.tail = t
        self.size += 1
    #마지막노드 추가 : tail.link -> 추가된 마지막 노드의 링크로 이동/ 추가된 마지막 모드 주소 ->tail.link

    def search(self, trg): #trg가 몇번째 노드에 있는지.
        p = self.head
        t = None
        for i in range(self.size):
            if trg == p.name:
                t = i
            p = p.link
        return t #찾았으면 t = i, 못찾았으면 t = None 출구를 1개로 고정하는 용

    def searchNode(self, trg):
        p = self.head
        while True:
            if trg == p.name:
                return p
            if p == self.tail:
                return None
            p = p.link

    def deleteFront(self):
        if self.isEmpty(): #비었으면 삭제 불가
            raise EmptyError("Underflow") #예외를 발생 시키는 것
        else:
            self.head = self.head.link
            self.tail.link = self.head
            self.size -= 1

    def deleteRear(self, p): #p는 삭제하고자 하는 pointer
        if self.isEmpty():
            raise EmptyError("Underflow")
        else:
            if p == None:
                pass
            elif p.link != self.tail and p.link != self.head: #중간노드
                p.link = p.link.link
            elif p == self.tail: #p가 tail이면 head 삭제
                self.deleteFront()
            elif self.head == self.tail: #노드가 한개
                self.head = self.tail = None
            elif p == self.head: #p가 head면 tail을 삭제
                p.link = p.link.link
                self.tail = p
        # 맨뒤 삭제: tail = 앞노드주소, 앞노드.link = tail.link
        self.size -= 1

    def printCLL(self):
        p = self.head
        while p:
            if p != self.tail and p != None:
                print(p.name,"=> ", end='')
            elif p == self.tail: #tail 일때.
                print(p.name,"=> ",p.link.name)
                return
            else:
                pass
            p = p.link

#EmptyError 예외처리를 해주는 클래스
class EmptyError(Exception):
    pass
