import io
import sys

_INPUT = """\
6
3 87
1 10 100
2 49
1 7
10 123456789012345678
1 100 10000 1000000 100000000 10000000000 1000000000000 100000000000000 10000000000000000 1000000000000000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,X=map(int,input().split())
  A=list(map(int,input().split()))
  ans=10**100
  for i in range(N):
    tmpy=((X-1)//A[i]+1)*A[i]
    tmpyx=tmpy-X
    tmp=0
    for j in reversed(range(N)):
      cnt=tmpy//A[j]
      tmpy-=cnt*A[j]
      tmp+=cnt
    if i>0:
      for j in reversed(range(N)):
        cnt=tmpyx//A[j]
        tmpyx-=cnt*A[j]
        tmp+=cnt
    ans=min(ans,tmp)
  print(ans)