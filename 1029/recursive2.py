#10진수 받아 2진수 출력
def dec2bin(n):
    if n == 0:
        return 0
    else:
        dec2bin(n//2)
        print(n%2, end="")
        return

dec2bin(10)