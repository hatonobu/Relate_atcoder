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
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

S = li()
for i in range(7):
    if S[i+1] < S[i]:
        print("No")
        exit()
    if S[i] % 25 != 0:
        print("No")
        exit()
    if S[i] < 100 or S[i] > 675:
        print("No")
        exit()

if S[7] % 25 != 0 or (S[7] < 100 or S[7] > 675):
    print("No")
else:
    print("Yes")