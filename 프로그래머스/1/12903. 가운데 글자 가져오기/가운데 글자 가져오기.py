def solution(s):
    answer = ''
    a = list(s)
    b = len(a)//2
    if len(a)%2!=0:
        answer = str(a[b])
    else:
        answer = str(a[b-1])+str(a[b])
    return answer