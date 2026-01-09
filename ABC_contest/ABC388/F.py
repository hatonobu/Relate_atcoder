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

N,M,A,B = mi()
LR = lli(M)

dp = [False]*500
dp[0] = True
for i in range(1,450):
    for j in range(A,B+1):
        if i-j < 0:
            pass
        else:
            if dp[i-j] == True:
                dp[i] = True
                break

dev2 = [False]*20
dev2[0] = True
now = 1
for l,r in LR:
    width = r-l+1
    dev1 = [False]*20
    if l-now > 400:
        dev1 = [True]*20
    else:
        for i in range(20):
            if dev2[i] == True:
                for j in range(1,21):
                    if l-j > now:
                        if dp[l-j-now] == True:
                            dev1[-j] = True
    
    dev2 = [False]*20
    for i in range(20):
        if dev1[i] == True:
            for j in range(20):
                jump = (20-i) + width + (j+1)
                if A <= jump <= B:
                    dev2[j] = True 

    print(dev1)
    print(dev2)
    now = r+1