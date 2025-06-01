from collections import deque
N, M, V= map(int,input().split())

#깊이우선탐색, 정점방문처리, 출력

#인접 리스트 초기화
graph = [[] for _ in range(N+1)]

#간선 정보 입력
for _ in range(M):
	a, b = map(int,input().split())
	graph[a].append(b)
	graph[b].append(a)
	
# 작은 번호순 방문을 위한 정렬
for i in range(1,N+1):
	graph[i].sort()
	
visitedDFS = [False]*(N+1)
visitedBFS = [False]*(N+1)

#DFS 구현 - 재귀
def DFS(V,visitedDFS):
	print(V,end=' ')
	visitedDFS[V] = True
	
	#재귀
	for i in graph[V]:
		if not visitedDFS[i]:
	 		DFS(i,visitedDFS)
	
# BFS 구현 - 큐
def BFS(V,visitedBFS):
	visitedBFS[V] = True
	
	#큐
	queue = deque([V])
	
	while queue : #큐 꺼내서 출력
		current = queue.popleft()
		print(current, end = ' ')
		
		#방문처리, 큐 삽입
		for i in graph[current]:
			if not visitedBFS[i]:
				visitedBFS[i] = True
				queue.append(i)

#DFS 실행
DFS(V,visitedDFS)
print()
BFS(V,visitedBFS)