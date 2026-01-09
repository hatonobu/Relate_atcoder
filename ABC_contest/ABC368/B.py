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

N = ii()
A = li()

times = 0
while(True):
    num = 0
    for a in A:
        if a > 0:
            num += 1
        if num > 1:
            flag = False
            break
    if flag:
        break
    times += 1
    flag = True
    A.sort(reverse=True)
    A[0] -= 1
    A[1] -= 1

print(times)
