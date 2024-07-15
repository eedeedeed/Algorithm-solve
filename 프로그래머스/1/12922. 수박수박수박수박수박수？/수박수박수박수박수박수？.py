def solution(n):
    answer = ''
    #n이 만약 짝수면 몫만큼 수박 프린트
    #홀수면 몫만큼하고 나머지만큼 수 프린트
    if n%2 == 0:
        answer = '수박'*(n//2)
    else:
        answer = '수박'*(n//2)+'수'
    return answer