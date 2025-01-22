def solution(sizes):
    
    a, b = 0,0
    
    for i in range(len(sizes)):
        
        #만약 가로보다 세로가 크면(가로<세로) 가로세로를 교환한다.
        if sizes[i][0] < sizes[i][1] :
            sizes[i][0],sizes[i][1]=sizes[i][1], sizes[i][0]
        
        if sizes[i][0] >= a :
            a = sizes[i][0] #최대 가로 갱신
        if sizes[i][1] >= b :
            b = sizes[i][1] #최대 세로 갱신

    return a * b