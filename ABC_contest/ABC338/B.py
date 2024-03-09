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

d = defaultdict(int)

S = input()
for s in S:
    d[s] += 1
n = list(sorted(d.items(), key=lambda x: x[1],reverse=True))

ans = []
a,b = n[0]
ans.append(a)
for word,key in n[1:]:
    if key != b:
        break
    else:
        ans.append(word)

ans.sort()

print(ans[0])