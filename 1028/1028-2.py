#Lamda식 : 반복문을 단축
a = [1, 5, 7, 8, 10, 53, 77, 82]

#a라는 리스트에서 람다x에 맞는 값x 목록을 리스트형태로 넣는 것 : 반복문을 단축한것
even = list(filter(lambda x:(x % 2 == 0), a))
print(even)
#a에 있는 값 모두 x로 매핑 후 모두*10
tentimes = list(map(lambda x:x * 10, a))
print(tentimes)

print()
#딕셔너리
b = [[0,1,8],[7,9,3],[9,10,1],[2,4,5]]
print(b)
b.sort() #해당 리스트의 첫번째 값으로 정렬
print(b)
b.sort(key = lambda x:x[2]) #해당 리스트의 3번째 값을 기준으로 정렬
print(b)

print()
#수행시간 체크 현재시간 - 시작시간
import time
import random

#time모듈 안에 seed()현재시간을 받아줌
random.seed(time.time()) #시드값이 동일하면 매번 똑같은 값
statTime = time.time()

c=[]
for i in range(100):
    for j in range(10000):
        d=[]
        d.append(random.randint(1, 1000))
    c.append(d)
print("---%f seconds----" % (time.time()-statTime))