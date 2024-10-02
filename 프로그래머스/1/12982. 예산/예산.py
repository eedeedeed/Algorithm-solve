def solution(d, budget):
    sum = 0
    count = 0
    
    d.sort()
    
    for i in d:
        sum += i
        if sum <= budget:
            count +=1
        else:
            break;
        
    return count