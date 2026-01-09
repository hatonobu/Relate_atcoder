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

N,K = mi()
S = input()

check = [(k, len(list(g))) for k,g in itertools.groupby(S)]
now = 0

ans = []
for i in range(len(check)):
    num, length = check[i][0], check[i][1]
    if num == '1':
        now += 1
        ans.append("1"*length)
        if now == K:
            ans.append("0"*check[i-1][1])
    else:
        if now == K-1:
            pass
        else:
            ans.append("0"*length)
        
print("".join(ans))
        