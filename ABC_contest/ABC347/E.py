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

N,Q = mi()
x = li()
S_num = [0]
ans = [0]*N
check = set()
d = defaultdict(list)
for i in range(Q):
    xx = x[i]
    check.add(xx)
    if d[xx]:
        num = d[xx].pop()
        ans[xx-1] += S_num[i] - S_num[num]
        check.remove(xx)
    else:
        d[xx].append(i)
    S_num.append(S_num[-1] + len(check))

for x,n in d.items():
    if len(n) > 0:
        num = n.pop()
        ans[x-1] += S_num[-1] - S_num[num]

print(*ans)

