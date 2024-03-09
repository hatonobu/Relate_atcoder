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

def max_sleighs(N, R, queries):
    # ソリの必要なトナカイの数をソート
    sorted_R = sorted(R)
    
    # 各ソリに必要なトナカイの数の累積和を計算
    cumulative_sum = [0] * (N+1)
    for i in range(1, N+1):
        cumulative_sum[i] = cumulative_sum[i-1] + sorted_R[i-1]
    
    result = []
    for X in queries:
        # 二分探索
        left = 0
        right = N
        while left <= right:
            mid = (left + right) // 2
            sleighs = cumulative_sum[mid]
            if sleighs <= X:
                left = mid + 1
            else:
                right = mid - 1
        
        result.append(left - 1)
    
    return result

N,Q = mi()
R = li()
q = lli(Q)
ans = max_sleighs(N,R,q)

print(*ans,sep="\n")