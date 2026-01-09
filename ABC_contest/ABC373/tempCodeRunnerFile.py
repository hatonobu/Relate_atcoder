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
B = A[:]
B.sort()
check = B[-M+1:]
ans = []
total = sum(A)
P = K - total

if M == 1:
    n = max(A)
    for i in A:
        if n-i > P:
            ans.append(-1)
        else:
            ans.append((n-i+1 + ((P-(n-i+1)) // 2)))


ruiseki = []
ruiseki.append(B[-M+1] - B[-M])
n = 1
for i in range(M-1,1,-1):
    if B[-i] == B[-i+1]:
        n += 1
    else:
        sa = B[-i+1] - B[-i]
        ruiseki.append(ruiseki[-1] + sa * n)
        for i in range(n-1):
            ruiseki.append(ruiseki[-1])
        n = 1

for i in A:
    now = P
    num = 0
    if check[0] > i:
        now -= check[0] - i + 1
        num += check[0] - i + 1
        idx = bisect.bisect_right(ruiseki,now)
        num += ruiseki[idx - 1] // idx 
    else:
        idx = bisect.bisect_right(check,i)
        now += ruiseki[idx-1]
        num -= idx
        idx = bisect.bisect_right(ruiseki,now)
        num += ruiseki[idx - 1] // idx
    ans.append(num)
print(*ans)