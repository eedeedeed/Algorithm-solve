def solution(arr):
    answer = []
    if len(arr) == 1:
        return [-1]
    
    min_value = min(arr)  # 배열에서 가장 작은 수를 찾습니다.
    arr.remove(min_value)
    
    answer = arr
    
    return answer