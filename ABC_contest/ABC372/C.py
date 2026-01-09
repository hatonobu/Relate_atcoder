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

N,Q = mi()
S = input()
total = 0
for i in range(N-2):
    if S[i:i+3] == "ABC":
        total += 1

ans = []
S = list(S)
for i in range(Q):
    a,b = ml()
    a = int(a)
    a -= 1
    num = 0
    if S[a] == "A":
        if a > N-3:
            pass
        elif S[a+1] == "B" and S[a+2] == "C":
           num -= 1 
    elif S[a] == "B":
        if a < 1 or a > N-2:
            pass
        elif S[a-1] == "A" and S[a+1] == "C":
            num -= 1
    elif S[a] == "C":
        if a < 2 or a > N-1:
            pass
        elif S[a-2] == "A" and S[a-1] == "B":
            num -= 1
    
    if b == "A":
        if a > N-3:
            pass
        elif S[a+1] == "B" and S[a+2] == "C":
           num += 1 
    elif b == "B":
        if a < 1 or a > N-2:
            pass
        elif S[a-1] == "A" and S[a+1] == "C":
            num += 1
    elif b == "C":
        if a < 2 or a > N-1:
            pass
        elif S[a-2] == "A" and S[a-1] == "B":
            num += 1
    else:
        pass
    total = total + num
    ans.append(total)
    S[a] = b

print(*ans,sep="\n")