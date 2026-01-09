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

N,K = mi()
S = list(input())
cnt = 0
for i in range(N):
    if S[i] == "o":
        cnt += 1
        if i != N-1:
            if S[i+1] == "?":
                S[i+1] = "."
        if i != 0:
            if S[i-1] == "?":
                S[i-1] = "."

if cnt == K:
    for i in range(N):
        if S[i] == "?":
            S[i] = "."
    print("".join(S))
    exit()
    
cnt_q = 0
lis = []
free = 0
for i in range(N):
    if S[i] == "?":
        cnt_q += 1
    else:
        if cnt_q != 0:
            if cnt_q % 2 == 0:
                cnt += cnt_q // 2
            else:
                cnt += (cnt_q // 2) + 1
                lis.append((cnt_q,i-cnt_q))
        cnt_q = 0   

if cnt_q != 0:
    if cnt_q % 2 == 0:
        cnt += cnt_q // 2
    else:
        cnt += (cnt_q // 2) + 1
        lis.append((cnt_q,N-cnt_q))

if cnt == K:
    for num, place in lis:
        for i in range(num):
            if i % 2 == 0:
                S[i+place] = "o"
            else:
                S[i+place] = "."
        
print("".join(S))
