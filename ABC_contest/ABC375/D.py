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

S = input()
ans = 0
check = [[] for _ in range(26)]
for i in range(len(S)):
    check[ord(S[i]) - ord("A")].append(i)

for i in range(len(S)):
    for j in range(26):
        if len(check[j]) > 1:
            left = bisect.bisect_left(check[j],i)
            right = len(check[j]) - bisect.bisect_right(check[j],i)
            ans += left * right
            
print(ans)