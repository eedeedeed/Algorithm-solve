def solution(x):
    answer = True

    
    #x 자릿수 합 구하기
    a = list(str(x))
    b = 0
    for i in a :
        b += int(i)
    if x%b !=0 :
        answer = False
    return answer