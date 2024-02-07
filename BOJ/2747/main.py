import sys
from collections import deque

n = int(sys.stdin.readline())
if n == 1:
	print(1)
	exit()
fib = deque()
fib.append(0)
fib.append(1)
for _ in range(n-1):
	t = fib.popleft()
	fib.append(t+fib[0])

print(fib[1])
