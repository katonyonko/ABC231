import io
import sys

_INPUT = """\
6
5
snuke
snuke
takahashi
takahashi
takahashi
5
takahashi
takahashi
aoki
takahashi
snuke
1
a
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import defaultdict
  N=int(input())
  dic=defaultdict(int)
  for i in range(N):
    S=input()
    dic[S]+=1
  ans=''
  cnt=0
  for key in dic:
    if dic[key]>cnt:
      cnt=dic[key]
      ans=key
  print(ans)