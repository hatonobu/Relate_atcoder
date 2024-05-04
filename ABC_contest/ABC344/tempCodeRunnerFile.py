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

T = input()
N = ii()
ans = [INF]*(len(T)+5)
ans[0] = 0
ans_new = [INF]*(len(T)+5)
ans_new[0] = 0

for i in range(N):
    A = li_st()
    for s in A[1:]:
        for j in range(len(T)):
            if ans[j] != INF:
                judge = True
                for k in range(len(s)):
                    if j+k >= len(T):
                        judge = False
                        break
                    if T[j+k] != s[k]:
                        judge = False
                        break
                if judge:
                    ans_new[j+len(s)] = min(ans[j] + 1,ans[j+len(s)])
    ans = ans_new[::]

print(ans[len(T)])