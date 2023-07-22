import sys
from collections import deque,defaultdict
import itertools
import heapq
import bisect
import queue

input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

N,P,Q = mi()
D = li()

ans = min(P,Q+min(D))
print(ans)