def solution(n):
    answer = 0
    answerr= ""
    listt = list(str(n))
    listt.sort(reverse=True)
    for i in listt:
        answerr+= i
    answer = int(answerr)
    return answer