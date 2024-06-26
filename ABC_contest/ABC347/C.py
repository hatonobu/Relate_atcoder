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

N,A,B = mi()
D = li()

for i in range(N):
    num = D[i] // (A+B)
    D[i] -= (A+B) * num
    if D[i] == 0:
        D[i] += (A+B)

ans = "Yes"
min_d = INF
max_d = -1
for d in D:
    min_d = min(min_d,d)
    max_d = max(max_d,d)

if max_d - min_d >= A:
    total = 0
    for d in D:
        if d > A:
            b_num = d
            break
        else:
            total = d
    if total + (A + B - b_num + 1) <= A:
        print("Yes")
    else:
        print("No")
else:
    print("Yes")
