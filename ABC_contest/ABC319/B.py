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

N = ii()
ans = []
for i in range(N):
    check = False
    for j in range(1,10):
        if N % j == 0:
            if i % (N // j) == 0:
                ans.append(str(j))
                check = True
                break
    if check == False:
        ans.append("-")

ans.append("1")
print("".join(ans))
    


