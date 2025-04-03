from collections import deque
# 웜 바이러스에 걸리게 되는 컴퓨터 수 출력
# 첫 번째 입력 : 컴퓨터 총 수, 100이하의 양의 정수, 
N = int(input())
# 두번째 입력 : 연결되어있는 컴퓨터 쌍의 수 M
M = int(input())
# M번째 입력 : 이어진 컴퓨터 번호 쌍
#X = computer = [[0 for _ in range(N+1)] for _ in range(N+1)]
computer = [[] for _ in range(N+1)]

for i in range(M):
    a , b = map(int,input().split())
    computer[a].append(b)
    computer[b].append(a)
#1번 컴퓨터가 걸렸을 때라서 입력을 1로 고정
start = 1
#바이러스 걸린 컴퓨터 카운트 -> 방문확인ok
virus = []


#바이러스 걸린 컴퓨터 찾기
def search(start):
    queue = deque([start]) # [1]
    virus.append(start)

    while queue : 
        current = queue.popleft() # 1/[]
        for i in computer[current]: #i=2,5 135
            if i not in virus : #3
                virus.append(i)
                queue.append(i) # [2,5] 53
           
search(start)
print(len(virus)-1)