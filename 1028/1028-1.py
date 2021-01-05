#학생클래스 생성
#멤버변수[속성] private형(self.) Name, id

#getter[멤버변수값->외부]: name, id // get_변수명(self, 매개변수),주 목적은 리턴
#setter[멤버변수<-외부]: name
#생성자(init) 초기변수와 객체 생성시 초기값 설정
#str함수

#오버로딩 : 동일기능이지만 매개변수 형식의 차이(파이썬은 지원X 파이썬은 매개변수를 여러개 써놔도 한개, 두개만 넘기기 가능(자체가 오버로딩 지원))
#오버라이딩 : 상속에서 쓰임. 부모의 함수를 사용할 때

class Student:
    def __init__(self, name, id=10):
        self.name = name
        self.id = id
    def get_name(self):
        return self.name
    def get_id(self):
        return self.id
    def set_name(self, name):
        self.name = name

#클래스명만 썼을때 출력하고 싶은 것 정의
#안쓰면 객체가 생성된 시작주소가 출력됨 <__main__.Student object at 0x009F9FB0>
#다른 이름 같은 객체, 같은 이름 다른 객체 구분할때 주소 사용
    def __str__(self):
        return self.name + ", " + str(self.id)

if __name__ == '__main__':
    s1 = Student("박민경",100)
    print(s1.name)#지양
    print(s1.get_name())#이걸 더 선호
    s1.id = 200
    print(s1.id)

    s1.set_name('이구')
    print(s1)

    s2 = Student('박현정')
    print('매개변수로 자체 오버로딩', s2)