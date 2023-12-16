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

S = input()
q = deque()

for s in S:
    if len(q) < 2:
        q.append(s)
    else:
        if s == "C":
            if q[-1] == "B" and q[-2] == "A":
                q.pop()
                q.pop()
            else:
                q.append(s)
        else:
            q.append(s)

print("".join(q))