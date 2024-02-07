def solution(dot):
    alldot = [[3, 0, 2], [0, 0, 0], [4, 0 ,1]]
    dot = (dot[0] // abs(dot[0]) + 1, dot[1] // abs(dot[1]) + 1)
    return alldot[dot[0]][dot[1]]