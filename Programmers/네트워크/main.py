from collections import deque
def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    q = deque()
    for i in range(n):
        if visited[i]: continue
        answer += 1
        q.append(i)
        while q:
            now = q.popleft()
            if visited[now]: continue
            else:
                visited[now] = True
                for nextcomputeridx in range(n):
                    if now == nextcomputeridx: continue
                    if computers[now][nextcomputeridx]:
                        q.append(nextcomputeridx)

    return answer