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

K = ii()
S = input()
T = input()

now = 0
if len(S) == len(T):
    for i in range(len(S)):
        if S[i] != T[i]:
            now += 1
elif len(S)== len(T) + 1:
    for i in range(len(T)):
        while(now <= 1):
            if S[i + now] != T[i]:
                now += 1
            else:
                break
        if now >= 2:
            break
elif len(S) + 1 == len(T):
    for i in range(len(S)):
        while(now <= 1):
            if S[i] != T[i + now]:
                now += 1
            else:
                break
        if now >= 2:
            break
else:
    print("No")
    exit()

if now >= 2:
    print("No")
else:
    print("Yes")