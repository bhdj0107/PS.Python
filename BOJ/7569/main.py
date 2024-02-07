from collections import deque
import sys
M, N, H = map(int, sys.stdin.readline().split())

field = {}

dx = (1, 0, 0, -1, 0 ,0)
dy = (0, 1, 0, 0, -1 ,0)
dz = (0, 0, 1, 0, 0 ,-1)

q = deque()

for i in range(H):
	field[i] = {}
	for j in range(N):
		field[i][j] = list(map(int, sys.stdin.readline().split()))


for i in range(H):
	for j in range(N):
		for k in range(M):
			if field[i][j][k] == 1:
				q.append((k, j, i))

while q:
	x, y, z = q.popleft()
	for i in range(6):
		nx = x + dx[i]
		ny = y + dy[i]
		nz = z + dz[i]
		if nx < 0 or ny < 0 or nz < 0:
			continue
		if nx >= M  or ny >= N or nz >= H:
			continue
		if field[nz][ny][nx]:
			continue
		q.append((nx, ny, nz))
		field[nz][ny][nx] = field[z][y][x] + 1


ans = 0
for i in range(H):
	for j in range(N):
		if 0 in field[i][j]:
			print(-1)
			exit()
		ans = max(ans, max(field[i][j]))

print(ans - 1)
