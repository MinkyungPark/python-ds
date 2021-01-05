class SLList:
    #노드만들기 위해 클래스 안에 클래스
    class Node:
        def __init__(self, name, link):
            self.name = name
            self.link = link

    def __init__(self):
        self.head = None
        self.size = 0

    def size(self):
        return self.size

    def isEmpty(self): #비어있으면 삭제 불가
        return self.size == 0 #0이면 True 아니면 False

    def insertFront(self, name):
        if self.isEmpty(): #헤드가 없으면, 첫번째 노드에 주소xxx에 데이터 None 삽입
            self.head = self.Node(name, None)
        else: #헤드가 있으면, 헤드에 있는 값을 새로 삽입된 노드의 주소로 교체한다.
            self.head = self.Node(name, self.head)
            #넘겨받은 name과 링크에 헤드주소를 넣은 노드를 생성해 헤드에 넣기
        self.size += 1

    def insertRear(self, name, p): #name을 p다음에 삽입
        if p == None:
            self.insertFront(name)
        else: #삽입위치가 있다. 제일 마지막에 수행되는 부분
            p.link = SLList.Node(name, p.link)
        self.size += 1

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
        while p:
            if trg == p.name:
                return p
            p = p.link #못찾았으면 다음노드
        return None #변수t 추가하기 싫을 때

    def deleteFront(self):
        if self.isEmpty(): #비었으면 삭제 불가
            raise EmptyError("Underflow") #예외를 발생 시키는 것
        else:
            self.head = self.head.link
            self.size -= 1

    def deleteRear(self, p): #p는 삭제하고자 하는 pointer
        if self.isEmpty():
            raise EmptyError("Underflow")
        p.link = p.link.link
        self.size -= 1


    def printSLL(self):
        p = self.head
        while p:
            if p.link != None:
                print(p.name,"=> ", end='')
            else:
                print(p.name) #마지막 노드 일때.
            p = p.link #다음노드로 넘어감

#EmptyError 예외처리를 해주는 클래스
class EmptyError(Exception):
    pass
