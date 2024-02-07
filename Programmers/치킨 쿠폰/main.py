def solution(chicken):
    ans = 0
    coupone = chicken
    while coupone >= 10:
        ans += coupone // 10
        remain = coupone % 10
        coupone = remain + coupone // 10
    return ans
