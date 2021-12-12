import io
import sys

_INPUT = """\
6
1000
50
3141
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  D=int(input())
  print(D/100)