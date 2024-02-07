def solution(today, terms, privacies):
    today = today.split('.')
    today = int(today[2]) + int(today[1]) * 28 + int(today[0]) * 28 * 12
    
    terms = {i.split()[0]:int(i.split()[1]) for i in terms}
    
    def addDate(date, timelambda):
        date = date.split('.')
        date = int(date[2]) + int(date[1]) * 28 + int(date[0]) * 28 * 12
        
        forward = date + timelambda * 28
        return forward

    
    answer = []
    for i, privacy in enumerate(privacies):
        privacy = privacy.split(' ')
        forward = addDate(privacy[0], terms[privacy[1]])
        if today >= forward: answer.append(i+1)
    return answer
