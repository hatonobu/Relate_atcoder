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

N,D = mi()
A = li()
lis = [0] * (10**6+1)

for num in A:
    lis[num] += 1  

if D == 0:
    print(sum(max(x-1,0) for x in lis))
    exit() 

ans = 0
for i in range(D):
    if not lis[i::D]:
        continue
    x = [0] + lis[i::D]
    dp = [0] * (len(x)+1)
    for j in range(1,len(x)):
        dp[j+1] = min(dp[j-1] + x[j-1], dp[j] + x[j])
        
    ans += dp[-1]
    
print(ans)