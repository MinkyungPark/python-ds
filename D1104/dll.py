#double linked List 링크가 두개 llink, rlink
#LLink - Data1 - Data2 ... - RLink   Data가 몇개든 가능
#tail 없이. head,llink(이전 것), rlink(다음 것)  head.rlink.llink = head
#삽입 삭제가 single 보다 편리하지만 link두개 관리가 복잡
#첫 노드 rlink, llink = null / head llink = null, tail rlink = null


class DLList:
    #노드만들기 위해 클래스 안에 클래스
    class Node:
        def __init__(self, name, age, llink, rlink):
            self.name = name
            self.age = age
            self.llink = llink
            self.rlink = rlink

    def __init__(self):
        self.head = None
        self.size = 0

    def size(self):
        return self.size

    def isEmpty(self): #비어있으면 삭제 불가
        return self.size == 0 #0이면 True 아니면 False

    def insert(self, name, age, pos = ""):
        p = self.searchNode(pos) #p뒤에 Insert 4가지
        if self.isEmpty(): #최초삽입
            new = self.Node(name, age, None, None)
            self.head = new
            self.size += 1
        elif self.head != None and p == None: #첫노드 삽입
            new = self.Node(name, age, None, self.head)
            self.head.llink = new
            self.head = new
            self.size += 1
        elif p != None:
            if p.rlink != None: #중간노드
                new = self.Node(name, age, p, p.rlink)
                p.rlink.llink = new
                p.rlink = new
            else: #끝노드
                new = self.Node(name, age, p, None)
                p.rlink = new
            self.size += 1
        else :
            pass

    def search(self, trg): #trg가 몇번째 노드에 있는지.
        p = self.head
        t = None
        for i in range(self.size):
            if trg == p.name:
                t = i
            p = p.link
        return t #찾았으면 t = i, 못찾았으면 t = None 출구를 1개로 고정하는 용

    def searchNode(self, pos):
        p = self.head
        if pos == "":
            return None
        while True:
            if pos == p.name:
                return p
            p = p.rlink

    def delete(self, pos):
        target = self.searchNode(pos)
        if target == None:
            print("찾는 노드가 없다") #여기 안됨...
        elif target.llink == None and target.rlink == None: #노드 한개
            self.head = None
        elif target.llink == None and target.rlink != None: #첫노드 삭제
            self.head = target.rlink # = None
            target.rlink.llink = target.llink
        elif target.llink != None:
            if target.rlink != None: #중간노드
                target.llink.rlink = target.rlink
                target.rlink.llink = target.llink
            else: #끝노드
                target.llink.rlink = target.rlink # = None
        self.size -= 1

    def printDLL(self):
        p = self.head
        while p:
            if p.rlink != None and p != None:
                print(p.name, p.age,"=> ", end='')
            elif p.rlink == None and p != None:
                print(p.name, p.age)
                break
            else:
                print('노드가 없음')
            p = p.rlink

#EmptyError 예외처리를 해주는 클래스
class EmptyError(Exception):
    pass
