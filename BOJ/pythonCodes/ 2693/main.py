import sys
N = int(sys.stdin.readline())
for _ in range(N):
    inp = list(map(int, sys.stdin.readline().split()))
    inp.sort()
    print(inp[-3])
