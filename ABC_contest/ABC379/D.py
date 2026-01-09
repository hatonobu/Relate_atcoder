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

Q = ii()
q = deque()

total = 0
ans_lis = []
for i in range(Q):
    S = li()
    if S[0] == 1:
        q.append(0)
    elif S[0] == 2:
        T = S[1]
        q.append(-T)
        total += T
    else:
        H = S[1]
        ans = 0
        while(q):
            num = q.popleft()
            if num == 0:
                if total >= H:
                    ans += 1
                else:
                    q.appendleft(num)
                    break
            else:
                total += num
        ans_lis.append(ans)

print(*ans_lis, sep="\n")