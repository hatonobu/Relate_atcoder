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

N,K,P = mi()
cost = []
lis = []
for _ in range(N):
    l = li()
    cost.append(l[0])
    lis.append(l[1:])

dp = [dict() for _ in range(N+1)]
for i in range(N):
    dp[i][tuple([0]*K)] = 0

#(0,0.0)
#(0 1 2)
#(1,4,P)
# if (P,P,P) : ans
#d.get(tuple,inf)

for i in range(N):
    d = dp[i]
    num = [0]*K
    for name,c in d.items():
        t = name
        dp[i+1][name] = min(dp[i+1].get(name,10**18),c)
        for j in range(K):
            num[j] = min(P,t[j]+lis[i][j])
        #print(num,c + cost[i], dp[i].get(tuple(num),10**18), c + cost[i])
        dp[i+1][tuple(num)] = min(dp[i+1].get(tuple(num),10**18), c + cost[i])
    
check = tuple([P]*K)
ans = dp[N].get(check,-1)
print(ans)