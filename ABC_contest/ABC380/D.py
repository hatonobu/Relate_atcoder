import sys
from collections import deque,defaultdict
#import pypyjit
import itertools
import heapq
import bisect
import queue

#pypyjit.set_param("max_unroll_recursion=-1")
sys.setrecursionlimit(10 ** 9)
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
Q = ii()
K = li()
check = [len(S)]
now = len(S)
while(now <= 10**18):
    now *= 2
    check.append(now)

ans = []
for k in K:
    ansPlace = k-1
    idx = bisect.bisect_left(check,k) - 1
    times = 0
    while(ansPlace >= len(S)):
        if ansPlace >= check[idx]:
            times += 1
        ansPlace = ansPlace % check[idx]
        idx -= 1
             
    if times % 2 == 0:
        ans.append(S[(ansPlace) % len(S)])
    else:
        ans.append(S[(ansPlace) % len(S)].swapcase())

print(*ans)
