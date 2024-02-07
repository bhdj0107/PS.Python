def solution(name, yearning, photo):
    table = {}
            
    for i in range(len(name)):
        table[name[i]] = yearning[i]
    answer = []
    for p in photo:
        score = 0
        for name in p:
            if name in table:
                score += table[name]
        answer.append(score)
    return answer