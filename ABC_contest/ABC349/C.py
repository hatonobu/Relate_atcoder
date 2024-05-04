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

S = input()
T = input()
T = T.lower()

def check(s,t):
    n = len(t)
    now = 0
    for ss in s:
        if now == n:
            break
        if ss == t[now]:
            now += 1
    
    if now == n:
        return True
    else:
        return False

if T[-1] == "x":
    ans = check(S,T[:2])
else:
    ans = check(S,T)

if ans:
    print("Yes")
else:
    print("No")