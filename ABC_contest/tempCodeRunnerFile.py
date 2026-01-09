import sys
from collections import deque,defaultdict
#import pypyjit
import itertools
import heapq
import bisect
import queue

#pypyjit.set_param("max_unroll_recursion=-1")
#sys.setrecursionlimit(10 ** 9)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
ml = lambda: map(str, input().split())
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353
INF = 8 * 10**18

Q,Y = mi()
stack = []
S = li_st()

for s in S:
  if s.isdigit:
    stack.append(int(s))
  elif s == "X":
    stack.append(Y)
  else:
    a = stack.pop()
    b = stack.pop()
    if s == "+":
      stack.append(a*b)
    elif s == "max":
      stack.append(max(a,b))
    else:
      stack.append(min(a,b))

print(stack[0])
