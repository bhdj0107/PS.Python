from collections import deque
def solution(priorities, location):
    answer = 0
    priorities_count = [0 for _ in range(11)]
    for i in range(len(priorities)):
        priorities_count[priorities[i]] += 1

    q = deque()
    for task in range(len(priorities)):
        q.append(task)

    while q:
        now = q.popleft()
        now_priority = priorities[now]
        if sum(priorities_count[now_priority + 1:]):
            q.append(now)
        else:
            priorities_count[now_priority] -= 1
            answer += 1
            if now == location: return answer