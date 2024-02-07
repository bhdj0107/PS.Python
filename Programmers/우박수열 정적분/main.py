def solution(k, ranges):
    answer = []
    collatz = [k]
    
    while collatz[-1] != 1:
        if collatz[-1] % 2 == 0:
            collatz.append(collatz[-1] // 2)
        else:
            collatz.append(collatz[-1] * 3 + 1)
    
    for left, right in ranges:
        nowsize = 0
        right = len(collatz) + right - 1
        if left > right:
            answer.append(-1)
            continue
            
        for i in range(left, right):
            pass
            nowsize += (collatz[i] + collatz[i + 1]) / 2
        answer.append(nowsize)
        
        
    return answer