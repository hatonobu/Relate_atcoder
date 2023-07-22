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
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

N = int(input())
A = input()
zero, one = 0, 0
ans = 0

#縦で考えた時のDP(規則性)、0のとき全てが1になり、ひとつ0をたす。1のとき1が0になり、0が1になる、そして1をたす。
#0 0 1 1 0
#0→1→0→1→1
#  0→1→0→1
#    1→0→1
#      1→1
#        0
#0 1 2 2 4
#ans = 1 + 2 + 2 + 4 = 9

for a in A:
    if a == '0':
        zero, one = 1, zero + one
    else:
        zero, one = one, zero + 1

    ans += one

print(ans)