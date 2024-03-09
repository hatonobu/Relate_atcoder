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
S = input()
Q = ii()
lis = list(range(97,97+26))

for i in range(Q):
    a,b = ml()
    for i in range(26):
        if lis[i] == ord(a):
            lis[i] = ord(b)

ans = []
for s in S:
    ans.append(chr(lis[ord(s) - ord("a")]))

print("".join(ans))

