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

N,M = mi()

check = [ input() for _ in range(N)]
lis = [0]*N

for i in range(M):
    x = 0
    y = 0
    for j in range(N):
        if check[j][i] == "1":
            x += 1
        else:
            y += 1
    if x == 0 or y == 0:
        continue
    elif x > y:
        for j in range(N):
            if check[j][i] == "0":
                lis[j] += 1
    else:
        for j in range(N):
            if check[j][i] == "1":
                lis[j] += 1

ans_lis = []
for i in range(N):
    ans_lis.append((i+1,lis[i]))
ans_lis.sort(key=lambda x: x[1],reverse=True)

ans = []
max_num = ans_lis[0][1]
for i in range(N):
    if ans_lis[i][1] == max_num:
        ans.append(ans_lis[i][0])

ans.sort()
print(*ans)