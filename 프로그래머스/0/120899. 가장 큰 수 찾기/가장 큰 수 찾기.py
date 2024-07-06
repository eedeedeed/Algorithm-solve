def solution(array):
    answer = []
    big = array[0]
    index = 0
    for i in range(0,len(array)):
        if array[i]> big:
            big = array[i]
            index = i
            
    answer.append(big)
    answer.append(index)
    return answer