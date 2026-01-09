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

S = list(input())
T = list(input())

ans = []

num = []

for i in range(len(S)):
    if ord(S[i]) > ord(T[i]):
        num.append(i)

for i in range(len(S)-1,-1,-1):
    if ord(S[i]) < ord(T[i]):
        num.append(i)

for n in num:
    S[n] = T[n]
    ans.append("".join(S))

print(len(ans))
print(*ans,sep="\n")