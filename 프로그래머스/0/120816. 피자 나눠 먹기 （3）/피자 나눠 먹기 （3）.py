def solution(slice, n):
    answer = 0
    if n%slice ==0:
       answer = n/slice
    else:
        answer = int(n/slice)+1
        
    return answer

#n/slice 나머지가 0이면 몫만큼 시키고
#n/slice 나머지 0아니면 몫+1
