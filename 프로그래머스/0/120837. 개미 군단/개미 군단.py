def solution(hp):
    answer = 0
    #hp가 23이면
    top = hp // 5
    #hp를 5로 나눈 몫인 4가 top
    mid = (hp%5)//3
    # 5로 나누고 난 나머지 3을 또 3으로 나눈 몫이 mid
    low = hp -(top*5)-(mid*3)
    
    
    answer = top + mid + low
    return answer