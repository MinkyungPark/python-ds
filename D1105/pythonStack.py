stack = []

def push(item):
    stack.append(item)

def pop():
    if(len(stack) != 0):
        item = stack.pop(-1)
        return item

#return stack[-1] #뒤로 접근 idx끝이 -1

def peak():
    if(len(stack) != 0):
        return stack[-1] #제일 끝에꺼

def compute(op, op1, op2):
    if op == '*':
        return op1*op2
    elif op == '/':
        return op1/op2
    elif op == '+':
        return op1+op2
    elif op == '-':
        return op1-op2

def eval(exp):
    tokenlist = exp.split() #공백기준으로 분할 postfix = stack
    for token in (tokenlist):
        if token[0] in '0123456789': #첫번째가 숫자이면
            push(int(token))
        else: #숫자가 아닌경우
            operand2 = pop()
            operand1 = pop()
            res = compute(token, operand1, operand2)
            push(res)
    return pop()

print('1 2 + -> ', eval('1 2 +'))
expr = input('수식 입력 [ex : 1 2 +] -> ')
print(expr,'->', eval(expr))