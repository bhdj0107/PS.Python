from math import inf
def solution(n, s, a, b, fares):
    answer = inf
    dist = [[inf for _ in range(n + 1)] for _ in range(n + 1)]
    for fare in fares:
        fare_a, fare_b, distance = fare
        dist[fare_a][fare_b] = distance
        dist[fare_b][fare_a] = distance
    for i in range(1, n + 1):
        dist[i][i] = 0
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    for i in range(1, n + 1):
        answer = min(answer, dist[s][i] + dist[i][a] + dist[i][b])
    return answer