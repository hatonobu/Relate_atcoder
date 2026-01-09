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

S = input()
l = len(S)

ans = 0
for i in range(l):
    for j in range(i+1,l):
        for k in range(j+1,l):
            if j-i == k-j:
                if S[i] == "A" and S[j] == "B" and S[k] == "C":
                    ans += 1

print(ans)