def solution(board, moves):
    answer = 0
    restack = [[] for _ in range(len(board[0]))]
    box = []
    for i in range(len(board)):
        for j, doll in enumerate(board[-(i+1)]):
            if doll:
                restack[j].append(doll)
    board = restack
    
    for m in moves:
        m -= 1
        if board[m]:
            crane = board[m].pop()
        else: continue
        popped = -1
        if box:
            popped = box.pop()
        if crane == popped:
            answer += 2
            continue
        elif popped != -1:
            box.append(popped)
            box.append(crane)
        else:
            box.append(crane)
    return answer