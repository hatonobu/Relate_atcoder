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

ans = "Yes"
N = ii()
S = input()
if N % 2 == 0:
    ans = "No"

for i in range(((N+1) // 2)-1):
    if S[i] != "1":
        ans = "No"

if S[(N+1)//2 - 1] != "/":
    ans = "No"

for j in range((N+1) // 2, N):
    if S[j] != "2":
        ans = "No"

print(ans)