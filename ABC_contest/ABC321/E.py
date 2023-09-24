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

T = ii()
for i in range(T):
    N,X,K = mi()
    num = X
    times = 0
    judge_left = True
    while(num > 1):
        num //= 2
        times += 1

    if 2**times + 2**(times-1) - 1 > X:
        judge_left = True
    else:
        #right tree
        judge_left = False

    check = [times+K,times-K]
  