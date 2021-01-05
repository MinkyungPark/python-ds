from D1031.circularLL import CLList
#디렉토리명 숫자만 있으면 임포트안됨

if __name__ == '__main__':
    s = CLList()
    s.insertFront('아')
    s.insertFront('사')
    s.insertFront('바')
    s.insertFront('마')
    s.insertFront('라')
    s.insertFront('다')
    s.insertFront('나')
    s.insertFront('가')
    s.printCLL()
    p = s.searchNode('가')
    s.deleteRear(p)
    s.printCLL()
    p = s.searchNode('다')
    s.deleteRear(p)
    s.printCLL()
    p = s.searchNode('아')
    s.deleteRear(p)
    s.printCLL()