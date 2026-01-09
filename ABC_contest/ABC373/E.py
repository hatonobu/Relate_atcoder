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

N,M,K = mi()
A = li()
B = []
for i in range(N):
    B.append((A[i],i))
B.sort()
C = A[:]
C.sort()
ans = [0] * N
total = sum(A)
P = K - total
ruiseki = [0]
for i in C:
    ruiseki.append(ruiseki[-1] + i)


if M == N:
    print(*ans)
    exit()

else:
    for i,(num,id) in enumerate(B):
        left = -1
        right = P + 1
        while(abs(right - left) > 1):
            mid = (right + left) // 2
            rid = bisect.bisect_right(C, num + mid)
            lid = N - M - ( 1 if i >= N - M else 0)
            
            cnt = 0
            if rid > lid:
                cnt += (rid - lid) * (num + mid + 1) - (ruiseki[rid] - ruiseki[lid])
            
            if lid <= i < rid:
                cnt -= 1
            else:
                cnt += mid
            
            if (cnt > P):
                right = mid
            else:
                left = mid
        
        if left == P:
            ans[id] = -1
        else:
            ans[id] = right

            
print(*ans)            
            
