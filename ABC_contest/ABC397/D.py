import sys
from collections import deque,defaultdict
#import pypyjit
import itertools
import heapq
import bisect
import queue

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

N = ii()

def check(d):
    left = 0 
    right = 10**9
    while (abs(right - left) > 1):
        mid = (left + right) // 2
        if (3*d*mid*mid + 3*d*d*mid + d*d*d - N <= 0):
            left = mid
        else:
            right = mid
    if (3*d*left*left + 3*d*d*left + d*d*d - N == 0):
        return left
    return -1

for d in range(10**6):
    if d**3 > N:
        break
    else:
        k = check(d)
        if k > 0:
            print(k+d,k)
            exit()
print(-1)