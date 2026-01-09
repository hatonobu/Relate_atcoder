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
rle = [(int(k), len(list(g))) for k,g in itertools.groupby(S)]
ans = 0

for i in range(len(rle)-1):
    a,num1 = rle[i]
    b,num2 = rle[i+1]
    if a+1 == b:
        ans += min(num1,num2)

print(ans)