# BST(Binary Search Tree)
# 참고 : http://ejklike.github.io/2018/01/09/traversing-a-binary-tree-1.html
# 리스트의 첫 값이 root가 됨, 그 이후 부터는 원칙(왼쪽자식<root<오른쪽자식)에 따라 삽입되는 이진 트리
# 최대검색횟수 => depth(height)
# 사향트리 : 검색의 효율을 저하시킴.(깊이가 작을 수록 BTS의 성능을 향상시킨다)
#     사향트리에 대한 대책 : 3개의 값중 중간값을 root로 만듦
#                           L1-L2-L3....(L2를 root로 보냄:LL회전), R1-R2-R3....(R2를 root로 보냄:RR회전),
#                           L1-R2-L3...(L3를 root로 보냄:RL회전),  R1-L2-R3...(R3를 root로 보냄:LR회전)
# BST Insert : root에서 출발해서 link값이 None값을 만날때까지 비교(왼쪽자식<root<오른쪽자식)하면서 이동후 삽입
#     Delete : 1. 찾고자하는 Node를 검색후
#              2-1. 자식이 없는 경우 : Node 삭제후 부모의 left, right인지 확인후 부모Node의 link를 None으로 저장
#              2-2. 자식이 하나 : 자식Node를 부모Node link값으로 저장
#              2-3. 자식이 둘 : 왼쪽 자식Node를 대체
class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def get(self, key): # 검색
        return self.getItem(self.root, key)

    def getItem(self, node, key):
        if node == None:
            print('No Data, search error...')
            return None
        if node.key > key:
            return self.getItem(node.left, key)
        elif node.key < key:
            return self.getItem(node.right, key)
        else:   # searched
            return node.value

    def put(self, key, value):  # Node insert
        return self.putItem(self.root, key, value)

    def putItem(self, node, key, value):
        if node == None:
            return Node(key, value)
        if node.key > key:
            node.left = self.putItem(node.left, key, value)
        elif node.key < key:
            node.right = self.putItem(node.right, key, value)
        else:   # node.key == key 인 경우 : 1. 오류처리 or 2. 업데이트
            node.value = value
        return node

    def delete_min(self, node): # 현재 node의 아래쪽에 있는 tree에서 최소값 삭제(
        if node.left == None:
            return node.right
        node.left = self.delete_min(node.left)
        return node

    def min(self):  # 최소값 찾기
        if self.root == None:
            return None
        return self.minimum(self.root)

    def minimum(self, node):
        if node.left == None:   # 최소값은 트리의 왼쪽방향으로 찾음
            return node
        return self.minimum(node.left)

    def inorder(self, node):
        if node != None:
            if node.left:
                self.inorder(node.left)
            print('['+str(node.key)+', '+node.value+']', end='')
            if node.right:
                self.inorder(node.right)

    def max(self):  # 최대값 찾기
        if self.root == None:
            return None
        return self.maximum(self.root)

    def maximum(self, node):
        if node.right == None:   # 최대값은 트리의 오른쪽방향으로 찾음
            return node
        return self.maximum(node.right)

    def delete(self, key):
        self.root = self.delNode(self.root, key)

    def delNode(self, node, key):
        if node == None:
            return None
        if node.key > key:
            node.left = self.delNode(node.left, key)
        elif node.key < key:
            node.right = self.delNode(node.right, key)
        else:   # 삭제하고자 하는 Node를 찾은 경우(,  ,  3.자노드가 2개인 경우)
            if node.right == None:  #   1.오른쪽 자노드가 없거나 하나도 없는 경우
                return node.left
            elif node.left == None: #   2.왼쪽 자노드가 없는 경우
                return node.right
            else:
                temp = node
                node = self.minimum(temp.right)     # 트리의 오른쪽에 있는 최소값이 현재위치로 보냄
                node.right = self.delete_min(temp.right)    # 위의 행에서 최소값이 삭제된 node로 옮겨졌으므로 옮겨진 최소값을 트리 아래쪽에서 삭제한다.
                node.left = temp.left   #  삭제된 node의 왼쪽 link를 새로운 node 왼쪽 link로 연결
                # node = self.maximum(temp.left)     # 트리의 왼쪽에 있는 최대값이 현재위치로 보냄
                # node.left = self.delete_max(temp.left)    # 위의 행에서 최대값이 삭제된 node로 옮겨졌으므로 옮겨진 최대값을 트리 아래쪽에서 삭제한다.
                # node.right = temp.right   #  삭제된 node의 오른쪽 link를 새로운 노드의 오른쪽 link로 연결
        return node

    def printB(self, node):
        if node != None:
            print('['+str(node.key)+','+node.value+']', end=' ')
            if node.left:
                print(str(node.key)+'(L):', end='')
                self.printB(node.left)
                print(end=' ')
            if node.right:
                print(str(node.key)+'(R):', end='')
                self.printB(node.right)
                print(end=' ')

if __name__ == '__main__':
    b = BST()
    b.root = b.put(21,'a')
    b.put(28,'b')
    b.put(14,'c')
    b.put(32,'d')
    b.put(25,'e')
    b.put(18,'f')
    b.put(11,'g')
    b.put(30,'h')
    b.put(19,'i')
    b.put(15,'j')
    b.put(29,'k')
    b.put(17,'l')

    print('BTS tree = ', end='')
    b.printB(b.root)

    print()
    b.delete(30)
    print('BTS tree(30 del) = ', end='')
    b.printB(b.root)

    print()
    b.delete(14)
    print('BTS tree(14 del) = ', end='')
    b.printB(b.root)

    print()
    b.put(33,'x')
    print('BTS tree(33 put) = ', end='')
    b.printB(b.root)
