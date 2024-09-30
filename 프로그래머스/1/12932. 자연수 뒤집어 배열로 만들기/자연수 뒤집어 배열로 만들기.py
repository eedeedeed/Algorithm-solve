def solution(n):
    answer = []
    bb = list(str(n)) #[1,2,3,4,5]
    #print(bb) #['1', '2', '3', '4', '5']
    for i in range(len(bb)-1,-1,-1):
        answer.append(int(bb[i]))
    return answer