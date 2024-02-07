from math import inf
def solution(m, n, startX, startY, balls):
    answer = []
    def flip(ballX, ballY):
        flipable_pos = []
        # minus_x filp
        if not (ballY == startY and ballX < startX):
            flipable_pos.append((ballX * -1, ballY))
        
        # minus_y flip
        if not (ballX == startX and ballY < startY):
            flipable_pos.append((ballX, ballY * -1))
        
        # plus_x flip
        if not (ballY == startY and ballX > startX):
            flipable_pos.append((2 * m - ballX, ballY))
        
        # plus_y flip
        if not (ballX == startX and ballY > startY):
            flipable_pos.append((ballX, 2 * n - ballY))
        return flipable_pos
    
    def dist(ball):
        return abs(ball[0] - startX) ** 2 + abs(ball[1] - startY) ** 2
    
    for ball in balls:
        shortest = inf
        ableBallpos = flip(*ball)
        for ableBall in ableBallpos:
            shortest = min(shortest, dist(ableBall))
        answer.append(shortest)
            
    return answer