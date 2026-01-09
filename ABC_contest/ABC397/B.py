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

now = 0
end = len(S)

ans = 0
while(now < end):
    if S[now] == "i":
        now += 1
    else:
       ans += 1 
    if now < end and S[now] == "o":
        now += 1
    else:
        ans += 1

print(ans)