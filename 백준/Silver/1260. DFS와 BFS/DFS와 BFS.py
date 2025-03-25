# N : 정점 개수
# M : 간선 개수
# V : 탐색을 시작할 정점의 번호

# 처음 입력받는게 N,M,V
# M번만큼 또 입력받음.

# 방문 정점이 여러 개일 때 정점 번호 작은 순으로 방문

# DFS : 깊이우선, 스택,재귀
# BFS : 너비우선, 큐 사용

from collections import deque

#첫 줄 입력
N, M, V = map(int,input().split())

#그래프 나타내기
graph = [[] for _ in range(N+1)]

#간선 수,관계 입력 받기
for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


#오름차순 정렬
for n in range(1,N+1):
    graph[n].sort()

# 방문처리 리스트 생성
visitedDFS = [False] * (N+1)
visitedBFS = [False] * (N+1)

def DFS(V):
    print(V, end = " ")
    visitedDFS[V] = True

    for i in graph[V] : # 이 부분에서 깊이 파고든다.
        if visitedDFS[i] == False :
            DFS(i)

def BFS(V):
    visitedBFS[V] = True
    queue = deque([V])

    while queue :
        i = queue.popleft()
        print(i, end= ' ')
        for g in graph[i]:
            if visitedBFS[g] == False :
                visitedBFS[g] = True
                queue.append(g)


DFS(V)
print()
BFS(V)