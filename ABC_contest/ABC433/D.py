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

N,M = mi()
mod = M
A = li()
#桁数での辞書→あまり見る
num_keta_dict = dict()
ans = 0
for a in A:
    num_keta_dict[(len(str(a)),a%mod)] = num_keta_dict.get((len(str(a)),a%mod),0) + 1

for a in A:
    for i in range(1,11):
        m = (M - (a*10**i % mod)) % mod
        ans += num_keta_dict.get((i,m),0)

print(ans) 
