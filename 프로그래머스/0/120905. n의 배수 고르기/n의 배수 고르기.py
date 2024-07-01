def solution(n, numlist):
    answer = []
    for i in range(0,len(numlist)):
        if numlist[i] % n == 0:
            answer.append(numlist[i])
    return answer