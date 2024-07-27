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

N,L,R = mi()
print("? 0 " + str(R+1),flush=True)
num = ii()
print("? 0 " + str(L),flush=True)
num2 = ii()

ans = (num - num2) % 100
print("! " + str(ans),flush=True)