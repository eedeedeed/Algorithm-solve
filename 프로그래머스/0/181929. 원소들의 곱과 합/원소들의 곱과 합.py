def solution(num_list):
    answer = 0
    sum = 0
    x = 1
    for i in num_list:
        sum+= i
        x = x*i
    if x<(sum*sum):
        answer = 1
    elif x> (sum*sum):
        answer =0
    return answer