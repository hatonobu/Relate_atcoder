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

N = ii()
lis = []
for i in range(20):
    lis.append(9*10**i)
    lis.append(9*10**i)

total = 1
now = 0
while (total < N):
    total += lis[now]
    now += 1

if now == 0:
    print(0)
    exit()
else:
    total -= lis[now-1]
    check = N - total - 1
    ans = []
    n = (now-1) // 2
    num = (check // 10**n) + 1
    ans.append(str(num))
    check -= (num - 1) * 10**n
    for i in range(n-1,-1,-1):
        num = (check // 10**i)
        ans.append(str(num))
        check -= num* 10**i
    if now % 2 == 0:
        c = ans + ans[::-1]
        s = "".join(c)
        print(s)
    else:
        c = ans[:-1] + ans[-1:] + ans[:-1][::-1]
        s = "".join(c)
        print(s)