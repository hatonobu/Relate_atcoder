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

N = ii()
S = input()
ruiseki = [0]

for i in range(N):
    num = int(S[i])
    ruiseki.append(ruiseki[-1] + num*(i+1))

ans = deque()
for i in range(N,-1,-1):
    ans.appendleft(ruiseki[i] % 10)
    ruiseki[i-1] += ruiseki[i] // 10

while(True):
    if ans[0] == 0:
        ans.popleft()
    else:
        break

print("".join(map(str,ans)))