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
tx = [li() for _ in range(N)]
need = defaultdict(int)

ans = []
K = 0
total = 0
for t,x in tx[::-1]:
    if t == 1:
        if need[x]:
            need[x] -= 1
            total -= 1
            ans.append(1)
        else:
            ans.append(0)
    elif t == 2:
        need[x] += 1
        total += 1
        K = max(K,total)

for key,value in need.items():
    if value != 0:
        print(-1)
        exit()

print(K)
print(*ans[::-1])