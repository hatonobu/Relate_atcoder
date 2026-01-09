import sys
from collections import deque,defaultdict
#import pypyjit
import itertools
import heapq
import bisect
import queue
import math

#pypyjit.set_param("max_unroll_recursion=-1")
sys.setrecursionlimit(10 ** 9)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
ml = lambda: map(str, input().split())
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353
INF = 8 * 10**18

R = ii()

ans = 0
def check_inside(x,y):
    if (2*x+1)**2 + (2*y+1)**2 <= 4*R**2:
        return True
    else:
        return False

x = R
ans = 4 * (R-1) + 1
for i in range(1,R):
    while(check_inside(x,i) == False):
        x -= 1
    ans += 4*x

print(ans)       