def solution(n, m):
    answer = []
    a = 0
    b = 0
    for i in range(1,n+1):
        if n%i==0 and m%i ==0:
            a=i
    # 두 수의 배수중 가장 작은 것
    b = m*n//a
    
    answer.append(a)
    answer.append(b)
    
    return answer