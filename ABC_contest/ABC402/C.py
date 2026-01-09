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

N,M = mi()
A = []
for i in range(M):
    a = li()
    A.append(a[1:])
B = li()
d = defaultdict(list)

for i,lis in enumerate(A):
    for num in lis:
        d[num].append(i)

check = set()
ans_lis = []
for num in B[::-1]:
    ans_lis.append(M - len(check))
    for n in d[num]:
        check.add(n)

print(*ans_lis[::-1],sep="\n")
    