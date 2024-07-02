def solution(n, k):
    answer = 0
    a = n//10
    k -= a
    answer = n*12000+k*2000
    return answer

#a는 10인분씩 몇 번 먹었는지 음료수서비스 개수
