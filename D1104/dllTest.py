from D1104.dll import DLList

if __name__ == '__main__':
    s = DLList()
    s.insert('가', 12)
    s.insert('사', 24)
    s.insert('다', 33)
    s.printDLL()
    s.insert('중간 삽입', 55, '사')
    s.printDLL()
    s.insert('끝에 삽입', 17,'가')
    s.printDLL()
    s.delete('다')
    s.printDLL()
    s.delete('중간 삽입')
    s.printDLL()
    s.delete('끝에 삽입')
    s.printDLL()
