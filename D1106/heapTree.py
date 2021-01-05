#binaryHeap
#list : 1,2,3,4,5,6,7,8,9
#i의 자식 : 왼쪽 i*2 오른쪽 i*2+1  /  i의 부모노드 i//2

class BinHeap:
    def __init__(self, a): #a는 들어오는 data
        self.a = a # a[0]는 사용하지 않는 것으로
        self.N = len(a) - 1 #a[0]사용하지 않기 때문

    def createHeap(self):
        for i in range(self.N//2, 0, -1):
            self.downHeap(i)

    def insert(self, key):
        self.N += 1
        self.a.append(key)
        self.upHeap(self.N) #마지막에 추가되었으므로 올라가면서 heap재구성

    def deleteMin(self): #루테이 있는 값 삭제
        if self.N == 0: #힙이 비어있는 상태
            print('underflow')
            return None
        min = self.a[1] #첫번째에 있는 값 [0]아니고 [1]임
        self.a[1], self.a[-1] = self.a[-1], self.a[1] # a, b = 1, 2 ->> a=1, b=2
        del self.a[-1]
        self.N -= 1
        self.downHeap(1) #1부터 downHeap
        return min

#최소힙은 자식 중 더 작은 값과 비교, 최대힙은 큰 값과 비교

    def downHeap(self, i): #i는 현재위치
        while 2*i <= self.N: #i의 왼쪽 자식이 힙에 있을 동안 반복
            iChild = 2*i #leftchild
            if iChild < self.N and self.a[iChild][0] > self.a[iChild+1][0]:
                #ichild+1 = rightchild
                #a[leftchild][0]은 key / a[leftchild][1]은 데이터 ex a[[],[10, 'apple'],[12, 'orange']]
                iChild += 1
            if self.a[i][0] < self.a[iChild][0]: #부노드와 자노드 비교
                break #자식이 크면 안바꿈
            else: #자식이 더 작으면 바꾼다
                self.a[i], self.a[iChild] = self.a[iChild], self.a[i]
                i = iChild

    def upHeap(self, i): #i = 1이면 루트
        while i > 1 and self.a[i//2][0] > self.a[i][0]:
            self.a[i//2], self.a[i] = self.a[i], self.a[i//2] #부<->자
            i = i//2 #부모로 올라가 또 비교

    def printHeap(self):
        print('MinHeap -> ', end='')
        for i in range(1, self.N+1):
            print('[%d:%s]' % (int(self.a[i][0]), self.a[i][1]), end='')
        print()
        print('Heap Size -> ', self.N)


if __name__ == '__main__':
    def menu():
        print('=============MENU==============')
        print('1.INSERT 2.DELETE 3.PRINT 0.EXIT')
        print('===============================')
        print("select menu : ", end='')

    a = [None]*1 #a=[[]]
    bh = BinHeap(a)
    bh.createHeap()

    while True:
        menu()
        sel = int(input())
        if sel == 1:
            key = input('key입력 : ')
            fruit = input('삽입할 과일 : ')
            hlist = [key, fruit]
            bh.insert(hlist)
        elif sel == 2:
            print('root : ', bh.deleteMin(), '삭제')
        elif sel == 3:
            print('Heap 출력 : ')
            bh.printHeap()
        elif sel == 0:
            exit(0)
        else: print('wrong select')


    # a = [None]*1 #a=[[]]
    # a.append([93,'민경'])
    # a.append([96,'현정'])
    # a.append([94,'경빈'])
    # a.append([20,'혜연'])
    # a.append([97,'세환'])
    # a.append([98,'김준'])
    # a.append([92,'성민'])
    # a.append([91,'용택'])
    # a.append([16,'현무'])
    # a.append([18,'세연'])
    # a.append([100,'영숙'])
    # a.append([102,'형모'])
    #
    # bh = BinHeap(a)
    # print('힙 구성 전의 트리 확인')
    # bh.printHeap()
    # bh.createHeap()
    #
    # print('최소힙')
    # bh.printHeap()
    #
    # print('Root삭제')
    # print('삭제된 Root', bh.deleteMin())
    # bh.printHeap()