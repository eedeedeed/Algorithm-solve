def solution(x, n):
    answer = []
    if x>0:
        answer = [x * i for i in range(1, n + 1)]
    else:
        answer = [x * i for i in range(1, n + 1)]
        answer.sort(reverse=True)
    return answer