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

N = ii()
S = input()

s = 1000000
t = -1

check = [True]*N
s_q = deque()
ans_q = deque()

for i,st in enumerate(S):
    if st == "(":
        s_q.append(i)
    elif st == ")":
        if s_q:
            n = s_q.pop()
            ans_q.append((n,i+1))

while(ans_q):
    l,r = ans_q.pop()
    if check[l] == False and check[r] == False:
        pass
    else:
        for i in range(l,r):
            check[i] = False

ans = []
for i in range(N):
    if check[i]:
        ans.append(S[i])
print(*ans,sep="")
