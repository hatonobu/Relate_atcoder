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
ml = lambda: map(str, input().split())
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

N = ii()
A = li()

#
#p[0]=1  p[1] = 1/N    p[2] = (1+1/N) * 1/N
#sp[0]=1 sp[1] = 1 + 1/N sp[2] = (1+1/N) + ((1+1/N) * (1/N))
#sp[i-1] * p[i] をすることで確実に今いるAiの値を含む期待値を取得できる
#一方で、次を考える際にAiを含まない時も考える必要があるので、sp[i-1] + p[i] を行うことで全確率を網羅できる

p = [0]*(N+1)
sp = [0]*(N+1)
p[0] = 1
sp[0] = 1
inv = pow(N,-1,mod)

ans = 0
for i in range(1,N+1):
    p[i] = (sp[i-1] * inv) % mod
    sp[i] = sp[i-1] + p[i]
    ans += A[i-1] * p[i]
    ans %= mod

print(ans)
