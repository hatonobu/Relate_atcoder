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

T = ii()
    
for _ in range(T):
    N = ii()
    S = "0" + input()
    lis = [False] * (2**N)
    lis[0] = True 
    for i in range(2**N):
        if lis[i] == False:
            continue
        else:
            for j in range(N):
                if i + 2**j >= 2**N:
                    break
                if i & 2**j:
                    continue
                else:
                    if S[i + 2**j] == "0":
                        lis[i + 2**j] = True
                    
    if lis[2**N-1] == True:
        print("Yes")
    else:
        print("No")