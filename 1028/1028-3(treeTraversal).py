#Data Structure
#객체 생성해서 할 예정 선형(연접리스트(리스트, 배열), 연결리스트(스택, 큐, 덱)), 비선형(트리, 그래프)

#1 이진트리 운행법(노드 : 주소, 값, 자식)
#pre, in, post ㅣ ㅡ ㅣ
#스택은 postfix
#일반 트리는 자식하나만 부모랑 연결 후 자식끼리 연결해 모든 트리를 이진트리로 구현 가능

class Node:
    def __init__(self, name, left = None, right = None): #name = data
        self.name = name
        self.left = left
        self.right = right

def map():
    n1 = Node("H")
    n2 = Node("F")
    n3 = Node("S")
    n4 = Node("U")
    n5 = Node("E")
    n6 = Node("Z")
    n7 = Node("K")
    n8 = Node("N")
    n9 = Node("A")
    n10 = Node("Y")
    n11 = Node("T")
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n4.left = n8
    n4.right = n9
    n5.left = n10
    n5.right = n11

    return n1 #루트를 리턴

def preOrder(n):
    if n != None:
        print(n.name + ' => ', end="")
        preOrder(n.left)
        preOrder(n.right)

def inOrder(n):
    if n != None:
        inOrder(n.left)
        print(n.name + ' => ', end="")
        inOrder(n.right)

def postOrder(n):
    if n != None:
        postOrder(n.left)
        postOrder(n.right)
        print(n.name + ' => ', end="")

start = map()
print('Preorder :\t', end="")
preOrder(start)
print()

start = map()
print('Inorder :\t', end="")
inOrder(start)
print()

start = map()
print('Postorder :\t', end="")
postOrder(start)
