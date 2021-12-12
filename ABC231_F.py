import io
import sys

_INPUT = """\
6
3
50 100 150
1 3 2
3
123456789 123456 123
987 987654 987654321
10
3 1 4 1 5 9 2 6 5 3
2 7 1 8 2 8 1 8 2 8
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  class BIT:
    def __init__(self, n):
        self._n = n
        self.data = [0] * n
    def add(self, p, x):
        assert 0 <= p < self._n
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p
    def sum(self, l, r):
        assert 0 <= l <= r <= self._n
        return self._sum(r) - self._sum(l)
    def _sum(self, r):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s
  N=int(input())
  A=list(map(int,input().split()))
  B=list(map(int,input().split()))
  X=[[A[i],B[i]] for i in range(N)]
  X.sort(key=lambda x: -x[1])
  X.sort(key=lambda x: x[0])
  x=list(set([X[i][0] for i in range(N)]))
  y=list(set([X[i][1] for i in range(N)]))
  x.sort()
  y.sort()
  dicx={x[i]:i for i in range(len(x))}
  dicy={y[i]:i for i in range(len(y))}
  X=[[dicx[X[i][0]], dicy[X[i][1]]] for i in range(N)]
  ans=0
  nowx=0
  pp=0
  ppp=0
  nowxtmp=BIT(len(y))
  tmp=BIT(len(y))
  for i in range(N):
    p,q=X[i]
    if p==nowx:
      ans+=pp-tmp.sum(0,q-1)
      ans+=pp-nowxtmp.sum(0,q)
      t=nowxtmp.sum(q,q)
      if t<3: ans+=1
      else: ans+=t
      nowxtmp[q]+=1
    else:
      