def solution(n):
    answer = []
    for i in range(1,n+1) :
        if(i%2 == 1):
            answer.append(i)
    return answer

# n이 10이면 answer에 1,3,5,7,9 담을거야
# i =1부터 10까지 반복할건데
# i가 홀수면 answer에 담기