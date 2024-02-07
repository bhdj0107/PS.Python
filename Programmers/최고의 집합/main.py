def solution(n, s):
        return [-1] if n > s else [s // n for _ in range(n - s % n)] + [s // n + 1 for _ in range(s % n)]