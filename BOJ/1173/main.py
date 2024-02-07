import sys
N, m, M, T, R = map(int,sys.stdin.readline().split())
if T > M - m:
    print(-1)
    exit()
queue = [(m, N, 0)]
def heart(before):
    if before - R < m:
        return m
    return before - R
while 1:
    now = queue[0]
    del queue[0]

    if now[1] == 0:
        print(now[2])
        exit()

    if not now[0] + T > M:
        queue.append((now[0]+ T, now[1] - 1, now[2] + 1))
    else:
        queue.append((heart(now[0]), now[1], now[2] + 1))
