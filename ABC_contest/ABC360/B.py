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

S,T = ml()
for i in range(1,len(S)):
    for k in range(i):
        ans = []
        for j in range(k,len(S),i):
            ans.append(S[j])
        check = "".join(ans)
        if check == T:
            print("Yes")
            exit()

print("No")