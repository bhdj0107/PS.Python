class BinaryTree:
    def __init__(self):
        self.value = None
        self.children = []
        self.sheep = None
        self.parent = None
    def create(self, value, sheep):
        self.value = value
        self.sheep = sheep
        return self

ans = -1
all_nodes = []
def backtracking(now, visited, sheeps, wolves):
    global ans
    visitable = []
    # 백트래킹 연산을 할 때마다, 양의 값을 최대치로 갱신한다.
    ans = max(ans, sheeps)

    # 부모가 이미 방문되어 이제는 갈 수 있는 길이 생긴 노드들을 모은다
    if not visited[0]:
        visitable.append(0)
    else:
        for isVisitable in range(1, len(visited)):
            if visited[all_nodes[isVisitable].parent] and not visited[isVisitable]:
                visitable.append(isVisitable)

    # 방문 가능한 노드들을 전부 들르면서
    for nextVisit in visitable:
        # 해당 노드가 양이라면
        # 그냥 들러간다
        if all_nodes[nextVisit].sheep:
            visited[nextVisit] = True
            backtracking(nextVisit, visited, sheeps + 1, wolves)
            visited[nextVisit] = False

        # 늑대라면
        else:
            # 만약 현재 노드를 방문 하고 나서도 양이 늑대보다 많다면, 해당 노드를 방문한다.
            if sheeps > wolves + 1:
                visited[nextVisit] = True
                backtracking(nextVisit, visited, sheeps, wolves + 1)
                visited[nextVisit] = False

def solution(info, edges):
    global all_nodes
    all_nodes = [BinaryTree.create(BinaryTree(), i, int(not(info[i]))) for i in range(len(info))]

    for parent, child in edges:
        all_nodes[parent].children.append(all_nodes[child])
        all_nodes[child].parent = parent

    backtracking(-1, [False for _ in range(len(all_nodes))], 0, 0)
    return ans