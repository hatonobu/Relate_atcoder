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
S = set([input() for _ in range(N)])

ans = 2 * len(S)
for i in S:
    flag = False
    for j in range(len(i)//2):
        if i[j] != i[-j-1]:
            flag = True
            break
    if flag == True:
        if i[::-1] in S:
            ans -= 1
            continue

print(ans//2)