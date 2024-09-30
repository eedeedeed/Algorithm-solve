def solution(n):
    answer = -1
    a = n**(1/2)
    if (a==int(a)):
        answer = ((a+1)**2)
    return answer