from collections import deque
#DFS 구현하기 (Depth First Search)
#BFS 구현하기 (Breath First Search)
# 1. stack / 2. set / 3. find out adj nodes.
# 1. queue / 


def dfs(graph,start):
  route = []
  stack = [start]
  visited = set()

  while stack:
    vertex = stack.pop()
    if vertex not in visited:
      route.append(vertex)
      visited.add(vertex)
    

return route

def bfs(graph,start,visited):
  q = deque([start])
  visited[start] = True
  
  while q:
    vertex = q.popleft()
    for i in graph[vertex]:
      if not in visited[i]:
        q.append(i)
        visited[i] = True
graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = False * 9

print(bfs(graph,1,visited))


#Eating frozen icecream

def dfs(x,y):
  if x <= -1 or x >=n or y <= -1 or y >= m:
    return False
  if graph[x][y] == 0:
    
    graph[x][y] = 1
    dfs(x-1,y) 
    dfs(x, y-1)
    dfs(x+1,y)
    dfs(x, y+1)
    return True
  return False
# create n x m matrix 
# n reprensts column m reprensts row 
n,m = map(int,input().split())

graph = []
for i in range(n):
  graph.append(list(map(int,input())))

res = 0
for i in range(n):
  for j in range(m):
    if dfs(i,j) == True:
      res +=1

  
# Escape a maze
n,m = map(int,input().split())

graph= []
for i in range(n):
  graph.append(list(map(int,input())))

dx = [-1,1,0,0] # left and right
dy = [0,0,-1,1] # down and up 
print(bfs(0,0))

def bfs(x,y):
  queue = deque()
  queue.append((x,y))
  while queue:
    x,y = queue.popleft()
    print(x,y)
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >=m:
        continue
      if graph[x][y] == 0:
        continue
      #only cares about x,y =1 
      if graph[x][y] == 1:
        graph[nx][ny] = graph[x][y] +1
        queue.append((nx,ny))
  return graph[n-1][m-1]
