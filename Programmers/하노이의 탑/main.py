import sys
sys.setrecursionlimit(10**8)
ans = []
maxn = -1
def hanoi(n, src, dest):
    global ans, maxn
    maxn = max(maxn, n)
    if n == 1:
        ans.append([src, dest])
    else:
        mid = [0, 1, 2, 3]
        mid[src], mid[dest] = 0, 0
        hanoi(n-1, src, sum(mid))
        ans.append([src, dest])
        hanoi(n-1, sum(mid), dest)
    if maxn == n: return ans
def solution(n):
    return hanoi(n, 1, 3)
