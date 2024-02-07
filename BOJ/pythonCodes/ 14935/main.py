import sys
N = sys.stdin.readline().rstrip()
while 1:
    bN = N
    N = str(int(N[0]) * len(N))
    if len(bN) == 1:
        break
if bN == N:
    print("FA")
else:
    print("NFA")
