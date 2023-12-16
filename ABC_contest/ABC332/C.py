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

N,M = mi()
S = input()

ans = 0
num = 0
check = 0
for i in range(N):
    if S[i] == "0":
        check = 0
        ans = max(ans,num)
        num = 0
    elif S[i] == "1":
        if check < M:
            check += 1
        else:
            num += 1
    elif S[i] == "2":
        num += 1


print(max(ans,num))