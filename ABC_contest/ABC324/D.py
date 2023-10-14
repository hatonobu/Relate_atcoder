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

N = ii()
S = input()
lis = [0]*10
for s in S:
    lis[int(s)] += 1

check = []
for i in range(10**7+5):
    if i*i >= 10**14:
        break
    else:
        check.append(str(i*i))

ans = 0
for s in check:
    l = [0]*10
    if N-lis[0] <= len(s) <= N:
        for ss in s:
            l[int(ss)] += 1
        flag = True
        for i in range(1,10):
            if lis[i] != l[i]:
                flag = False
                break
        if flag:
            ans += 1

print(ans)

