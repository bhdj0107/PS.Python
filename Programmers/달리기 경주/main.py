def solution(players, callings):
    rank = {}
    for i, name in enumerate(players):
        rank[name] = i
    
    for call in callings:
        back = rank[call]
        front = back - 1
        
        f_name = players[front]
        
        players[front], players[back] = players[back], players[front]
        
        rank[call] = front
        rank[f_name] = back

    answer = players
    return answer