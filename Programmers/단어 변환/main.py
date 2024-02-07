from collections import deque
def solution(begin, target, words):
    words.append(begin)
    maps = {i:{j:0 for j in words} for i in words}
    dist = {i:0 for i in words}
    for a in words:
        for b in words:
            count = 0
            for k in range(len(a)):
                count += int(a[k] != b[k])
            if count == 1:
                maps[a][b] = 1
                maps[b][a] = 1
    q = deque()
    visited = {}
    for i in words:
        visited[i] = False
    q.append((begin, 0))
    while q:
        now, distance = q.popleft()
        if visited[now]: continue
        else:
            visited[now] = True
            dist[now] = distance
            for nextword in maps[now]:
                if maps[now][nextword]: q.append((nextword, distance + 1))
    if dist.get(target):
        return dist[target]
    else:
        return 0