from collections import deque
def solution(n, wires):
    field = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for src, dest in wires:
        field[src][dest] = 1
        field[dest][src] = 1
    ans = n + 1
    for disconnect in wires:
        discon_a, discon_b = disconnect
        field[discon_a][discon_b] = 0
        field[discon_b][discon_a] = 0

        q = deque()
        visited = [False for _ in range(n + 1)]
        visited[1] = True
        for i in range(1, n + 1):
            if field[1][i]: q.append((1, i))

        while q:
            parent, child = q.popleft()
            visited[parent] = True
            if visited[child] == False:
                for i in range(1, n + 1):
                    if field[child][i]: q.append((child, i))
        ans = min(ans, abs(n - sum(visited) * 2))
        field[discon_a][discon_b] = 1
        field[discon_b][discon_a] = 1
    return ans