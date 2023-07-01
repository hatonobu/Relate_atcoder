import sys
from collections import deque,defaultdict
import itertools
import heapq
import bisect
import queue

#sys.setrecursionlimit(10 ** 9)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

N = ii()
A = li()
S = input()

def mex(a,b,c):
  for i in range(4):
    if a != i and b != i and c != i: 
       return i

dp1 = [0]*3
dp2 = [[0]*3 for _ in range(3)]

ans = 0
for i,s in enumerate(S):
    num = A[i]
    if s == "M":
        dp1[num] += 1
    elif s == "E":
        for j in range(3):
           dp2[num][j] += dp1[j]
    elif s == "X":
        for k in range(3):
           for l in range(3):
              ans += mex(k,l,num) * dp2[k][l]
    else:
       pass

print(ans)