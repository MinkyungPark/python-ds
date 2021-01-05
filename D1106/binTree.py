#이진트리
#null link = n+1

class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def preOrder(self, n): #n에 맨 처음에는 root가 넘어옴
        if n!= None:
            print(str(n.item), ' ', end='') #출력위치가 맨 첨
            if n.left != None: #왼쪽 끝까지 갔다가 오른쪽
                self.preOrder(n.left)
            if n.right != None:
                self.preOrder(n.right)

    def inOrder(self, n):
        if n != None:
            if n.left != None:  # 왼쪽 끝까지 갔다가 오른쪽
                self.inOrder(n.left)
            print(str(n.item), ' ', end='') #출력위치가 가운데
            if n.right != None:
                self.inOrder(n.right)

    def postOrder(self, n):
        if n != None:
            if n.left != None:  # 왼쪽 끝까지 갔다가 오른쪽
                self.postOrder(n.left)
            if n.right != None:
                self.postOrder(n.right)
            print(str(n.item), ' ', end='') #출력위치가 맨 뒤

    def levelOrder(self, root): #재귀X
        q = []
        q.append(root)
        while len(q) != 0:
            t = q.pop(0) #q의 맨 첫번째 item을 t에 담음/ 부모가 나가고
            print(str(t.item),' ',end='')
            if t.left != None: #부모의 왼쪽 자식 넣음
                q.append(t.left)
            if t.right != None: #부모의 오른쪽 자식 넣음
                q.append(t.right)

    def height(self, root):
        if root == None:
            return 0
        else:
            return 1 + max(self.height(root.left)) + max(self.height(root.right))

    def size(self, root):
        if root == None:
            return 0
        else:
            return 1 + self.size(root.left) + self.size(root.right)

    def copyTree(self, n):
        if n == None:
            return None
        else:
            left = self.copyTree(n.left)
            right = self.copyTree(n.right)
            return Node(n.item, left, right) #마지막으로 루트가 생성되면서 리턴

    def isEqual(self, n, m): #copyTree로 생성된 트리 같은지 확인하려고
        if n == None and m == None:
            return n == m #True
        if n.item != m.item:
            return n == m #False
        return (self.isEqual(n.left, m.left)) and (self.isEqual(n.right, m.right))


if __name__ == '__main__':
    t = BinaryTree()
    n1 = Node('A')
    n2 = Node('B')
    n3 = Node('C')
    n4 = Node('D')
    n5 = Node('E')
    n6 = Node('F')
    n7 = Node('G')
    n8 = Node('H')
    n9 = Node('I')

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n4.left = n8
    n4.right = n9
    t.root = n1

    #print('Tree Height :', t.height(t.root))
    print('Tree Size :', t.size(t.root))

    u = BinaryTree()
    u.root = t.copyTree(t.root)
    print('t와 u비교', t.isEqual(t.root, u.root))
    print('PreOrder : ',end='')
    t.preOrder(t.root)
    print()
    print('InOrder : ', end='')
    t.preOrder(t.root)
    print()
    print('PostOrder : ', end='')
    t.postOrder(t.root)
    print()
    print('LevelOrder : ', end='')
    t.levelOrder(t.root)