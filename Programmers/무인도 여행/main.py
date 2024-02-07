from collections import deque
def solution(maps):
    islands = []
    width, height = len(maps[0]), len(maps)
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    delta = ((-1, 0), (1, 0), (0, 1), (0, -1))

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X':
                q = deque()
                lifedays = 0
                q.append((i, j))
                while q:
                    current_y, current_x = q.popleft()
                    if current_y < 0 or current_y >= height or current_x < 0 or current_x >= width: continue
                    if not visited[current_y][current_x]:
                        visited[current_y][current_x] = True
                        if maps[current_y][current_x] != 'X':
                            lifedays += int(maps[current_y][current_x])
                            for k in range(4):
                                q.append((current_y + delta[k][0], current_x + delta[k][1]))
                if lifedays:
                    islands.append(lifedays)
    if islands:
        return sorted(islands)
    else:
        return [-1]
