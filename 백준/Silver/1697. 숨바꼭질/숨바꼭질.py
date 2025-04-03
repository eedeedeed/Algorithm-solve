from collections import deque
N, M = map(int,input().split()) #5, 17



visited = [False]*100001

def BFS(N,M): # 5,17매개변수로 함수 실행
	queue = deque([N]) #큐에 5 삽입 생성
	visited[N] = True #5 방문처리
	sec = 0
	
	while queue:
		current_queue_len = len(queue) #현재 큐 길이는 1
		for _ in range(current_queue_len): #현재 큐에 있는 노드 개수만큼만 반복
			current = queue.popleft() #current ==5
			a = current -1 
			b = current +1 
			c = current *2
			temp = [a,b,c]
			for i in temp :
				if 0<=i<=100000 and visited[i] == False :
					if i == M : return sec+1
					queue.append(i)
					visited[i]=True
		sec+=1

if N==M:
	print(0)
else :
 print(BFS(N,M))