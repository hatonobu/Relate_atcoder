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
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

K = ii()

s = "0123456789"
lis = []

for e in itertools.product([0,1],repeat=10):
    st = []
    for i in range(10):
        if e[i] == 1:
            st.append(s[i])
    st.sort(reverse=True)
    ans = "".join(st)
    if ans:
        lis.append(int(ans))

lis.sort()
print(lis[K])

                                