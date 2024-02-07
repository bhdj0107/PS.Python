def solution(triangle):
    copy_tri = []
    for i in triangle:
        copy_tri.append([])
        for j in i:
            copy_tri[-1].append(j)
    for i in range(len(triangle) - 1):
        for j in range(len(triangle[i])):
            triangle[i+1][j] = max(triangle[i+1][j], copy_tri[i+1][j] + triangle[i][j])
            triangle[i+1][j+1] = max(triangle[i+1][j+1], copy_tri[i+1][j+1] + triangle[i][j])

    return max(triangle[-1])