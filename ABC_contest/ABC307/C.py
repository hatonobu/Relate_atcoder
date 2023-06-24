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

H,W = mi()
A = [input() for _ in range(H)]

H2,W2 = mi()
B = [input() for _ in range(H2)]

Hx,Wx = mi()
X = [input() for _ in range(Hx)]