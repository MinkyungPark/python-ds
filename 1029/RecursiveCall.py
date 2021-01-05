#venv 파이참에서 제공하는 가상머신
#아나콘다 가상머신 사용할 예정

#재귀적 호출(메모리문제 때문에 가급적 쓰지 않는 것이 좋음)
#어쩔 수 없이 써야 하는 경우는 함수 사이즈를 최소한으로 예)피보나치, 팩토리얼, 트리운행
#주의 : 반드시 내부에 종료조건을 포함하여야 한다.

print("-------------팩토리얼--------------")

def fac(n):
    if n <= 1: #재귀적 함수의 종료조건 부분
        return 1
    else:
        return n * fac(n-1) #재귀적 호출 부분

def loopFac(n):
    hap = 1
    for i in range(1, n+1):
        hap *= i
    return hap

print("fact(%d) =" % (5), fac(5))
print("fact(%d) =" % (5), loopFac(5))

#주기억 장치에 fac(5)는 다섯번, loopFac(5)는 한번

print()
print("-------------피보나치 수열--------------")

#1, 1, 2, 3, 5, 8, 13, 21, 34...
def fibonacci(n):
    if n <= 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

indata = int(input('수 입력 :'))
print("fibonacci = ", end="")
for i in range(1, indata + 1):
    print(fibonacci(i), end=" ")

#반복문으로 구현
f=[]
def loopfibo(n):
    for i in range(n):
        if i == 0:
            f.append(0)
        elif i == 1:
            f.append(1)
        else:
            f.append()
