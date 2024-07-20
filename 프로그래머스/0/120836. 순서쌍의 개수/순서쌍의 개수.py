def solution(n):
    answer = 0
    count = 0
    for i in range(1,n+1):
        if n%i ==0: #약수
            count += 1
            
    answer = count
    return answer