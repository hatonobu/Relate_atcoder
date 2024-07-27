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

N,T = mi()
S = input()
X = li()
check1 = []
check0 = []
check0_after = []

for i in range(N):
    if S[i] == "0":
        check0.append(X[i])
        check0_after.append(X[i] - T)
    else:
        check1.append(X[i])

check0.sort()
check0_after.sort()

ans = 0
for num in check1:
    start = bisect.bisect_right(check0,num)
    end = bisect.bisect_right(check0_after,num + T)
    ans += end - start

print(ans)
