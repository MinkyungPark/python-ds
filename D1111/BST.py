#Binary Search Tree
#left < Root < Right
#첫 값 -> 루트 , 그 이후 부터는 옆의 원칙에 따라 삽입되는 이진트리(루트부터 내려가서 작으면 왼쪽, 크면 오른쪽)
#깊이가 4이면 4안에 찾아진다.
#회전. LL RR LR RL 까지 해줘야 하지만 실습에서는 안함

#삽입 : 루트부터 null까지 이동 후 삽입
#삭제 : 노드 검색 후 결과에서 정책결정.(자노드가 없는 경우 : 노드 삭제 후 부모의 left, right인지 확인 후 None으로 세팅/
# 자노드가 한개인 경우 : 자노드를 현대 위치로 올려준다. / 자노드 두개 : 왼쪽 자노드를 대체 )

class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    #Search
    def get(self, k): # k는 key
        return self.getItem(self.root, k)

    def getItem(self, n, k): #node, key
        if n == None:
            return None
        elif n.key > k: #key가 더 작으면 왼쪽
            return self.getItem(n.left, k)
        elif n.key < k:
            return self.getItem(n.right, k)
        else: #n.key == k 찾은경우
            return n.value

    #Insert
    def put(self, key, value):
        return self.putItem(self.root, key, value)

    def putItem(self, n, k, v):
        if n == None:
            return Node(k, v)
        elif n.key > k:
            n.left = self.putItem(n.left, k, v)
        elif n.key < k:
            n.right = self.putItem(n.right, k, v)
        else: #같은 노드가 존재하는 경우 -> 삽입불가 or 갱신
            n.value = v
        return n

    #Delete
    #전체에서 최솟값 삭제
    def deleteMin(self, n):
        if n.root == None:
            print('Tree is Empty')
        self.root = self.delmin(self.root)

    #특정 노드 아래에서 최솟값 삭제
    def delmin(self, n):
        if n.left == None:
            return n.right
        n.left = self.delmin(n.left)
        return n

    def min(self): #최소값 찾기
        if self.root == None:
            return None
        return self.minimum(self.root)

    def minimum(self, n):
        if n.left == None:
            return n
        return self.minimum(n.left)

    def inOrder(self, n):
        if n != None:
            if n.left:
                self.inOrder(n.left)
            print('[' + str(n.key) + ',' + str(n.value) + ']', end='')
            if n.right:
                self.inOrder(n.right)

    def max(self):
        if self.root == None:
            return None
        return self.maximun(self.root)

    def maximum(self, n):
        if n.right == None:
            return n
        return self.maximum(n.right)

    #특정 노드 삭제
    def delete(self, k):
        self.root = self.delNode(self.root, k)

    def delNode(self, n, k):
        if n == None:
            return None
        elif n.key > k:
            n.left = self.delNode(n.left, k)
        elif n.key < k:
            n.right = self.delNode(n.right, k)
        else: #삭제할 노드를 찾음 1.오른쪽자노드 없거나 둘다 없 2.왼쪽 자노드 없 3.자노드두개
            if n.right == None:
                return n.left
            elif n.left == None:
                return n.right
            #자노드 두개인 경우. 오른쪽 최솟값을 삭제된 노드로 대체함.
            t = n
            n = self.minimum(t.right)
            n.right = self.delmin(t.right)
            n.left = t.left
            # 중간노드 삭제 할 때, 왼쪽노드의 자노드들 중 최댓값 올릴건지 or 오른쪽노드의 자노드들 중 최솟값 올릴건지
            # n = self.maximum(t.left)
            # n.left = self.deleteMax(t.left)
            # n.right = t.right
        return n

    def printBST(self, node):
        if node != None:
            print('['+str(node.key)+','+node.value+']', end=' ')
            if node.left:
                print(str(node.key)+'(L):', end='')
                self.printBST(node.left)
                print(end=' ')
            if node.right:
                print(str(node.key)+'(R):', end='')
                self.printBST(node.right)
                print(end=' ')