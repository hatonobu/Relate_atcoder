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
T = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ans = 0
for i in range(25):
    for j in range(26):
        if T[i] == S[j]:
            for k in range(26):
                if T[i+1] == S[k]:
                    ans += abs(j - k)

print(ans)
            