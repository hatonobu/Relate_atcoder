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

def kaibun(S):
    for j in range(len(S)//2):
        if S[j] != S[-j-1]:
            return False
    return True

for i in range(10**7):
    if i * i * i > N:
        a = i-1
        break

for i in range(a,0,-1):
    s = str(i**3)
    if kaibun(s):
        print(s)
        exit()