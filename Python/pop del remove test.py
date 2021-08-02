from time import time_ns


loop = 100000
print('loop:\t',loop)
print('list의 길이:',10)
print('--------------')
print('가장 뒤에 있는 원소를 없앨 경우')
start = time_ns()
for _ in range(loop):
    s = [2, 5, 3, 4, 9, 1, -3, 6, 12, 0]
    s.pop(9)
print('pop:\t',time_ns() - start)

start = time_ns()
for _ in range(loop):
    s = [2, 5, 3, 4, 9, 1, -3, 6, 12, 0]
    del s[9]
print('del:\t',time_ns() - start)

start = time_ns()
for _ in range(loop):
    s = [2, 5, 3, 4, 9, 1, -3, 6, 12, 0]
    s.remove(0)
print('remove:\t',time_ns() - start) 



print('--------------')
print('가장 앞에 있는 원소를 없앨 경우')
start = time_ns()
for _ in range(loop):
    s = [2, 5, 3, 4, 9, 1, -3, 6, 12, 0]
    s.pop(0)
print('pop:\t',time_ns() - start)

start = time_ns()
for _ in range(loop):
    s = [2, 5, 3, 4, 9, 1, -3, 6, 12, 0]
    del s[0]
print('del:\t',time_ns() - start)

start = time_ns()
for _ in range(loop):
    s = [2, 5, 3, 4, 9, 1, -3, 6, 12, 0]
    s.remove(2)
print('remove:\t',time_ns() - start)



print('--------------')
print('중간(index=4)에 있는 원소를 없앨 경우')
start = time_ns()
for _ in range(loop):
    s = [2, 5, 3, 4, 9, 1, -3, 6, 12, 0]
    s.pop(4)
print('pop:\t',time_ns() - start)

start = time_ns()
for _ in range(loop):
    s = [2, 5, 3, 4, 9, 1, -3, 6, 12, 0]
    del s[4]
print('del:\t',time_ns() - start)

start = time_ns()
for _ in range(loop):
    s = [2, 5, 3, 4, 9, 1, -3, 6, 12, 0]
    s.remove(9)
print('remove:\t',time_ns() - start)
