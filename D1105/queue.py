class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next # = link

front = rear = None
size = 0

def enque(item):
    global front
    global rear
    global size
    new = Node(item, None)
    if size == 0: #비었음
        front = rear = new
    else:
        rear.next = new
        rear = new
    size += 1

def deque():
    global front
    global rear
    global size
    if size != 0:
        front = front.next
        size -= 1
        if size == 1:
            rear = None #front이미 None
    else: #아무것도 없을 때
        print('underflow')

def printQueue():
    global front
    p = front
    print('Front <- ', end="")
    while p:
        if p.next != None and size != 0:
            print(p.item, end="")
        elif size == 0:
            print('underflow')
            break
        else:
            print(p.item, '<- Rear')
        p = p.next

if __name__ == '__main__':
    enque('가 ')
    enque('나 ')
    enque('다 ')
    enque('라 ')
    enque('마 ')
    printQueue()
    deque()
    printQueue()
