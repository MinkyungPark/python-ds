from collections import deque

dq = deque('data') #d, a, t, a 하나씩 들어감
dq.append('aaa')
dq.append('bbb')
dq.appendleft('bbb')
dq.append('ccc')
dq.appendleft('ccc')
dq.appendleft('eee')
for node in dq:
    print(node.upper(), end=" ")
print()


dq2 = deque()
dq2.append('fff')
dq2.appendleft('zzz')
dq2.appendleft('bbb')
dq2.append('aaa')
dq2.append('ggg')
dq2.append('hhh')
print(dq2)
dq2.pop()
print(dq2)
dq2.popleft()
print(dq2)
print(dq2[-1]) #맨끝
print(dq2[-2])
print(dq2[0])
print(dq2[-4])
print('aaa' in dq2)
print('a' in dq2)
dq2.extend('deque')
print(dq2)
dq2.extendleft(reversed('python'))
print(dq2)