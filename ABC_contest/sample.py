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
ml = lambda: map(str, input().split())
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

L,R = mi()
S = input()

ans = []
check = []

for i in range(len(S)):
    s = S[i]
    if L <= i+1 <= R:
        check.append(s)
    else:
        ans.append(s)

print("".join(ans[:L-1]),"".join(check[::-1]),"".join(ans[L-1:]),sep="")
