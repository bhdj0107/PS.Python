import sys
import copy
N = int(sys.stdin.readline())
inp = sys.stdin.readline().rstrip()
chk_idx = [i for i in range(len(inp))]
ans = list(inp)
for _ in range(N - 1):
    inp = sys.stdin.readline().rstrip()
    temp = copy.deepcopy(chk_idx)
    for i in chk_idx:
        if ans[i] != inp[i]:
           ans[i] = "?"
           temp.remove(i)
    check = copy.deepcopy(temp)

print("".join(ans))

