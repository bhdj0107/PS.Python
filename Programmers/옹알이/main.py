def solution(babbling):
    answer = 0
    able = set()
    able.update(['aya', 'ye', 'woo', 'ma'])
    for babble in babbling:
        while True:
            if len(babble) >= 2:
                if babble[:2] in able:
                    babble = babble[2:]
                    continue
                if babble[:3] in able:
                    babble = babble[3:]
                    continue
                break
            elif len(babble) == 0:
                answer += 1
                break
            else:
                break
    return answer