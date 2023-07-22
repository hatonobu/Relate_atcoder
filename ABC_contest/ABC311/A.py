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

N = ii()
S = input()

true = [False]*3
ans = 0

for a,n in enumerate(S,1):
    if n == "A" and true[0] == False:
        ans += 1
        true[0] = True
    elif n == "B" and true[1] == False:
        ans += 1
        true[1] = True
    elif n == "C" and true[2] == False:
        ans += 1
        true[2] = True
    
    if ans == 3:
        print(a)
        exit()
        