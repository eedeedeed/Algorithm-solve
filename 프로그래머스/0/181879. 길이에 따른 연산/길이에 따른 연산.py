def solution(num_list):
    answer = 1
    if len(num_list)>=11:
        for i in num_list:
            answer += i
        answer = answer-1   
    else:
        for i in num_list:
            answer = i * answer
    return answer