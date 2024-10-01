def solution(s):
    a = list(s)
    return  (len(a)==4 or len(a)==6) and s.isdigit()