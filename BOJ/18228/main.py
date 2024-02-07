import sys
def a():
    N = int(sys.stdin.readline())
    ice = tuple(map(int, sys.stdin.readline().split()))
    print(min(ice[:ice.index(-1)]) + min(ice[ice.index(-1) + 1:]))

a()
