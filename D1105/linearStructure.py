#선형리스트 스택, 큐, 덱
#Statck : LIFO 구현방법 1.링크드리스트 2.배열(파이썬에서는 리스트)
#삽입 - push 순서 :알고리즘, 0.오버플로우 유무 top >= (size - 1) 1.공간확보[객체 생성] 2.데이터입력, top증가
#삭제 - pop 순서 :알고리즘, 0.언더플로우 유무 top <= 0, top == bottom 01.데이터 출력 2.공간소거(garbage collection), top감소
#A,B,C,D,E를 push와 pop 가능한 순서
#->ABCDE EDCBA AEDCB BAEDC BACDE CBADE CBAED CBDAE CBDEA DCBAE DCEBA ..
#안되는 규칙 : 역순으로 2단계 차이나면 못뺌 CADBE, DBCAE, DABCE, ECABD

#Queue : FIFO front rear / enque deque
#enque -> rear++ / deque -> front++
#빈공간이 생긴다는 문제가 있음
#-> Moving Queue로 해결 rear - frant + 1 >= size
#-> 환영큐를 만들어버림림
#-> 링크드리스트로 구현

#DeQue : 덱 구조가 복잡하지만 가장 자연스러운 구조. 양쪽 다 삽입 삭제가 가능
#제한된 덱
#입력제한 덱 : Scroll 한군데서만 입력 / 출력제한 덱 : shelf