import sys
from collections import deque,defaultdict
import itertools
import heapq
import bisect
import queue
from functools import lru_cache 

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

N,A,X,Y =  mi()

@lru_cache
def f(n,a,x,y):
    if n == 0:
        return 0
    else:
        num1 = x + f(n//a,a,x,y)
        num2 = (y*6 + f(n//2,a,x,y) + f(n//3,a,x,y) + f(n//4,a,x,y) + f(n//5,a,x,y) + f(n//6,a,x,y)) / 5
        ans = min(num1,num2)

    return ans

print(f(N,A,X,Y)) 
