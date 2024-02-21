def solution(land):
  import sys
  sys.setrecursionlimit(1000000000)
  
  w,h = len(land[0])-1,len(land)-1
  visit = [[0 for x in range(len(land[0]))] for x in range(len(land))]
  def bfs(x,y,answer):
      global size
      global idx
      if visit[x][y] == 0:
          visit[x][y]=1
      else:
          return 0
      
      if land[x][y]==1:
          if idx not in answer[y]:
            answer[y].append(idx)
          size += 1
          
            
          if x-1 >= 0:
              #상
              bfs(x-1,y,answer)
          if x+1 <= h:
              #하
              bfs(x+1,y,answer)
          if y-1 >= 0:
              #좌
              bfs(x,y-1,answer)
          if y+1 <= w:
              #우
              bfs(x,y+1,answer)
  real_answer = [[] for x in range(len(land[0]))]
  sizes = []
  global idx
  idx = 0
  for x in range(len(land)):
      for y in range(len(land[0])):
          if land[x][y]==1 and visit[x][y]==0:
              global size
              size = 0
              bfs(x,y,real_answer)
              sizes.append(size)
              idx += 1
  variables = [0 for x in range(len(land[0]))]
  for x,y in enumerate(real_answer):
      variable = 0
      for z in y:
         variable += sizes[z]
      variables.append(variable)
  return max(variables)