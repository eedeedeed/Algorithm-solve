import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline  # 빠른 입력 처리

n, m, i = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 작은 정점부터 탐색하도록 정렬
for ii in range(1, n + 1):
    graph[ii].sort()

visited = [0] * (n+1)
order = 1

def dfs(start):
    global order
    visited[start] = order
    for e in graph[start]:
        if visited[e] == 0:
            order += 1
            dfs(e)

dfs(i)

for qq in range(1, n+1):
    print(visited[qq])
