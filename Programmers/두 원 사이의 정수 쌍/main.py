from math import sqrt, floor
def solution(r1, r2):
    answer = r2 - r1 + 1
    for i in range(1, r2):
        M = floor(sqrt(r2**2 - i**2))
        if i < r1:
            m = sqrt(r1**2 - i**2)
        else: m = 0
        answer += M - floor(m)
        if m % 1 == 0 and m != 0: answer += 1
    answer *= 4
    return answer