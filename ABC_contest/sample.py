import sys
from collections import deque,defaultdict
import itertools
import heapq
import bisect
import queue
import math

#sys.setrecursionlimit(10 ** 9)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
ml = lambda: map(str, input().split())
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

S1,S2,S3 = ml()
T1,T2,T3 = ml()

check = (S1 == T1) + (S2 == T2) + (S3 == T3)
if check == 0 or check == 3:
    print("Yes")
else:
    print("No")
        