import sys
from collections import deque,defaultdict
import itertools
import heapq
import bisect
import queue
import math

#sys.setrecursionlimit(10 ** 9)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

N = ii()
A = li()

avg = sum(A) / N
a = int(avg)
b = math.ceil(avg)


ans1 = 0
ans2 = 0
for num in A:
    if num <= a:
        ans1 += a-num
    elif num >= b:
        ans2 += num - b

print(max(ans1,ans2))