from D1030.sll import SLList

def menu():
    print("==============================MENU==============================")
    print("1.앞에삽입 2.뒤에삽입 3.처음삭제 4.선택삭제 5.검색 6.목록보기 0.종료")

if __name__ == '__main__':
    s = SLList()
    while True:
        menu()
        sel = int(input('Menu Select:'))
        if sel == 1: #앞에삽입
            data = input("삽입할 데이터 입력 :")
            s.insertFront(data)
            s.printSLL()
        elif sel == 2: #뒤에삽입
            data = input("삽입할 데이터 입력 :")
            pos = input("어디 뒤에 삽입 할지 :")
            p = s.searchNode(pos)
            s.insertRear(data, p)
            s.printSLL()
        elif sel == 3: #처음삭제
            s.deleteFront()
            s.printSLL()
        elif sel == 4: #선택삭제
            pos = input("삭제할 위치 입력(삭제할 위치 다음이 삭제됨) :")
            p = s.searchNode(pos)
            s.deleteRear(p)
            s.printSLL()
        elif sel == 5: #검색
            data = input("검색할 데이터 입력 :")
            pos = s.search(data)
            print(data+ "는"+str(pos+1)+"에 있음")
        elif sel == 6: #목록보기
            s.printSLL()
        elif sel == 0: #종료
            exit(0)
        else: print("잘못된 입력입니다.")