import sys
nums = list(map(int, sys.stdin.readline().rstrip()[:]))
nums.sort(reverse=True)
print("".join(map(str, nums)))

