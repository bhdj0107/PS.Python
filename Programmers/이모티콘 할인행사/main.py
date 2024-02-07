cnt, total = 0, 0
emtdis = []
emoticons = []
users = []
def recursion(D):
    global cnt, total, emtdis

    # if all discount percentages are setted
    if D == len(emoticons):
        tcnt, ttotal = 0, 0
        # cal for all users
        for tdiscount, tmoney in users:
            utotal = 0

            # buy all possible emoticons
            for i, dis in enumerate(emtdis):
                if dis >= tdiscount:
                    utotal += emoticons[i] * (100 - dis) // 100

            # check plus or buy
            if utotal >= tmoney:
                tcnt += 1
            else:
                ttotal += utotal

        # update cnt, total
        if tcnt > cnt:
            cnt, total = tcnt, ttotal
        elif tcnt == cnt:
            total = max(total, ttotal)

    else:
        for d in [10, 20, 30, 40]:
            emtdis[D] = d
            recursion(D+1)
            emtdis[D] = -1

def solution(us, emt):
    global users, emoticons, emtdis
    users = us
    emoticons = emt
    emtdis = [-1 for _ in range(len(emoticons))]
    recursion(0)
    return [cnt, total]