import io
import sys

_INPUT = """\
6
3 1
100 160 130
120
5 5
1 2 3 4 5
6
5
4
3
2
5 5
804289384 846930887 681692778 714636916 957747794
424238336
719885387
649760493
596516650
189641422
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from bisect import bisect_left
  N,Q=map(int,input().split())
  A=list(map(int,input().split()))
  A.sort()
  for i in range(Q):
    x=int(input())
    print(N-bisect_left(A,x))