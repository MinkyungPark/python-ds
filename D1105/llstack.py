#링크드리스트로 스택구현

class Node:
    def __init__(self, item, link):
        self.item = item
        self.link = link

#top과 size는 언제어디서나 같아야
top = None
size = 0

def push(item):
    global top
    global size
    #if max <= size: 사이즈를 정했을 때.
    top = Node(item, top)
    size += 1

def pop():
    global top
    global size
    if size != 0:
        top_item = top.item
        top = top.link
        size -= 1
        return top_item
    else:
        print("underflow")

def peak():
    #global top 쓸필요 없음. 지역에top없으므로 찾음
    #top의 값을 바꿀 땐 전역 지정
    if size != 0:
        return top.item
    else:
        return "underflow"

def printStack():
    print('Top -> \t', end='')
    p = top
    while p:
        if p.link != None:
            print(p.item, '-> ', end='')
        else:
            print(p.item)
        p = p.link


if __name__ == '__main__':
    push('가')
    push('나')
    printStack()
    pop()
    printStack()
    push('다')
    push('라')
    push('마')
    printStack()
    pop()
    pop()
    printStack()
    print(peak())
    pop()
    pop()
    print(peak())