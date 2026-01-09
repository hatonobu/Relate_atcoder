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
INF = 8 * 10**18

lis = [ "login", "logout", "public", "private" ]
N = ii()
isCheck = False
ans = 0
for _ in range(N):
    S = input()
    if S == lis[0]:
        isCheck = True
    elif S == lis[1]:
        isCheck = False
    elif S == lis[2]:
        pass
    elif S == lis[3]:
        if not isCheck:
            ans += 1

print(ans)