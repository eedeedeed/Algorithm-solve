def solution(cipher, code):
    answer = ''
    for i in range(len(cipher)):
         if (i+1) %code ==0:
            answer += cipher[i]
    return answer

#code의 배수번째 인덱스만 추가