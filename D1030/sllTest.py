from D1030.sll import SLList
#디렉토리명 숫자만 있으면 임포트안됨

if __name__ == '__main__':
    s = SLList()
    s.insertFront('♡ 도담')
    s.insertFront('김초롱')
    s.insertFront('박현정')
    s.insertFront('♡ 이구')
    s.insertFront('박민경')
    s.insertFront('임수진')
    s.insertFront('♡ 펭수')
    s.insertFront('임수진')
    s.printSLL()
    p = s.searchNode('임수진')
    s.insertRear('마이콜', p)
    s.printSLL()
    s.deleteFront()
    s.printSLL()
    p = s.searchNode('마이콜') #펭수를 삭제하기 위해서 마이콜을 넣어준 것.
    s.deleteRear(p)
    s.printSLL()