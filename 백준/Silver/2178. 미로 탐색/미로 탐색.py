from collections import deque

N,M = map(int,input().split())
maze = [[] for _ in range(N)]
for i in range(N): #0,1,2,3
    a = list(map(int,input()))
    maze[i] = a
  

startx, starty = 0 , 0
visited= [[False]*(M) for _ in range(N)]

distance=[[0]*M for _ in range(N)]

def search_min(i,j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True
    distance[i][j] =  1
    
    #상하좌우 방향벡터
    dx=[-1,1,0,0]
    dy = [0,0,1,-1]
    
    while queue :
        x,y = queue.popleft()
        for i in range(4):
            nx = x +dx[i]
            ny = y + dy[i]
            if 0<=nx <N and 0<=ny < M :
                if maze[nx][ny] ==1 and visited[nx][ny] == False :
                    visited[nx][ny] =True
                    distance[nx][ny] = distance[x][y]+1
                    queue.append((nx,ny))
                 
search_min(startx,starty)
print(distance[N-1][M-1])