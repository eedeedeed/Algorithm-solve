# recursionError 피하기 
# dfs 한번 호출 시 재귀깊이가 너무 깊어질때
#1) python 기본 재귀 깊이 1000 -> setrecursionlimit 설정
import sys
sys.setrecursionlimit(15000)

input = sys.stdin.readline # 빠른 입력받기

# 장마철에 올 수 있는 '모든 비의 양'에 대해서 그 중 '가장 안전 영역이 많은 것'을 찾으면 됩니다.

# 1. 첫 줄 입력받기 (변수n)
n = int(input())
# 2. n번만큼 입력 받기 -> graph[[]]에 저장
graph = [[] for _ in range(n+1)]

for i in range(n):
    graph[i] = list(map(int,input().split()))


def dfs(i,j,rain_level,visited) :
    visited[i][j] = True
    
    #상하좌우 탐색을 위한 좌표
    dx = [0,0,-1,1] #좌우
    dy = [-1,1,0,0] #상하
    
    for q in range(4):
        nx = i+dx[q]
        ny = j+dy[q]
        if 0<=(nx)<n and 0<=(ny)<n :
            if graph[nx][ny] > rain_level and visited[nx][ny] == False:
                dfs(nx,ny,rain_level,visited)
    return 1

# 1~100 비 높이에 완전 탐색
# 모든 비 높이에 대해서 안전영역 개수가 가장 많은 경우 그 영역개수를 출력

# graph[i][j]가 rain_level 보다 크고, visited[i][j]가 False이면 DFS(i,j)
# 안전영역개수의 변수 count

# 비 양(1~100)에 따른 안전구역개수 담은 리스트 생성
safe = []

max_height = 1
for i in range(n):
    for j in range(n):
        if max_height < graph[i][j] : 
            max_height = graph[i][j]       

for rain_level in range(0,max_height+1): #비가 안올수도 있음

    #강수량마다 초기화
    visited = [[False]*(n+1) for _ in range(n+1)]
    count = 0

    for i in range(n):
        for j in range(n):
             if graph[i][j] > rain_level and visited[i][j] == False :
                count += dfs(i,j,rain_level,visited)
    safe.append(count)

print(max(safe))


# MEMO--------------------------------------
# 원리 : DFS 함수 내에서는 방문처리 안되어있으면 방문처리하고 재귀호출하면됨.


# 비 양이 1인경우 후에 5인경우에서 True/False는 바뀌지 않음. >> 그대로 가져감.❌❌❌❌
# 비 양이 1인 경우 안전구역의 True 방문처리를 하면 비양2에서 pass해버림 -> 강수량마다 방문처리를 초기화해야됨⭕
# DFS로 한 안전구역 덩어리를 돌고나서 구역개수 += 1

 