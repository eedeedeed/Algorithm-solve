def solution(arr1, arr2):
    answer = 0
    arr1sum = 0
    arr2sum = 0
    for i in arr1:
        arr1sum += i
    for i in arr2:
        arr2sum += i
        
    if len(arr1)==len(arr2):
        if arr1sum > arr2sum :
            answer = 1
        elif arr1sum < arr2sum:
            answer = -1
        else:
            answer = 0
    elif len(arr1)>len(arr2):
        answer = 1
    elif len(arr1)<len(arr2):
        answer = -1
            
    return answer