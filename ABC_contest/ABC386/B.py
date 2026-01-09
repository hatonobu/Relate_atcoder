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
S += "xxxxx"

num = 0
ans = 0

while(True):
    if S[num] == "x":
        break
    else:
        if S[num] == "0" and S[num+1] == "0":
            num += 2
        else:
            num += 1
    ans += 1

print(ans)
        