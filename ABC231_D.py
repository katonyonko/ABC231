import io
import sys

_INPUT = """\
6
4 2
1 3
2 3
4 3
1 4
2 4
3 4
3 3
1 2
2 3
1 3
2 1
1 2
6 4
1 2
3 5
2 4
1 4
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  #BFS
  from collections import deque
  def bfs(G,s):
    D[s]=0
    node=0
    edge=0
    dq=deque()
    dq.append(s)
    while dq:
      x=dq.popleft()
      node+=1
      for y in G[x]:
        edge+=1
        if D[y]>D[x]+1:
          D[y]=D[x]+1
          dq.append(y)
    if edge==2*(node-1):
      return True
    else:
       return False
  N,M=map(int,input().split())
  inf=10**30
  D=[inf]*N
  G=[[] for _ in range(N)]
  for i in range(M):
    A,B=map(int,input().split())
    A-=1; B-=1
    G[A].append(B)
    G[B].append(A)
  ans='Yes'
  for i in range(N):
    if len(G[i])>2: ans='No'
    if D[i]!=inf: continue
    a=bfs(G,i)
    if a==False: ans='No'
  print(ans)