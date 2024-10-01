def solution(price, money, count):
    
    sum = 0
    
    for i in range(1, count+1):
        a = (price*i)
        sum += a
    
    if sum > money :
        answer = sum-money
    else:
        answer = 0
    return answer