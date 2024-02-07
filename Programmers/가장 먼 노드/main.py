from collections import deque
def solution(n, edge):
    answer = 0
    dist = [-1 for _ in range(n + 1)]
    dist[1] = 0
    linkmap = [set() for _ in range(n + 1)]
    for a,b in edge:
        linkmap[a].add(b)
        linkmap[b].add(a)

    q = deque()
    visited = [False for _ in range(n + 1)]
    q.append((1, 0))
    visited[1] = True

    while q:
        now, d = q.popleft()
        for i in linkmap[now]:
            if not visited[i]:
                visited[i] = True
                q.append((i, d + 1))
                dist[i] = d
    maxdist = max(dist)
    return dist.count(maxdist)