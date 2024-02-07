def solution(plans):
    answer = []
    todo = []
    delay = []
    for name, start, duration in plans:
        start = start.split(':')
        start = int(start[0]) * 60 + int(start[1])
        end = start + int(duration)
        todo.append([name, start, end])

    todo.sort(key=lambda x:x[1])

    nname, nstart, nend = todo[0]
    for name, start, end in todo[1:]:
        if nend - start > 0:
            delay.append((nname, nend - start))
            nname = name
            nend = end

        elif nend - start == 0:
            answer.append(nname)
            nname = name
            nend = end



        elif nend - start < 0:
            answer.append(nname)
            candodelay = start - nend
            while candodelay > 0:
                if delay:
                    dname, dtime = delay.pop()
                    if dtime > candodelay:
                        delay.append((dname, dtime - candodelay))
                        break
                    elif dtime == candodelay:
                        answer.append(dname)
                        break
                    elif dtime < candodelay:
                        candodelay -= dtime
                        answer.append(dname)
                else: break

            nname, nend = name, end

    answer.append(nname)
    while delay:
        answer.append(delay.pop()[0])


    return answer