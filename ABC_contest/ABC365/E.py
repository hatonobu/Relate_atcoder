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

N = ii()
A = li()
lis_string = []
for a in A:
    lis_string.append(str(format(a,"030b")))

check = [[0]*(N+3) for _ in range(30)]

ans = 0
for i in range(N-1,0,-1):
    for j in range(30):
        if lis_string[i][-1-j] == lis_string[i-1][-1-j]:
            check[j][i] = check[j][i+1]
            ans += check[j][i] * 2**j
        else:
            check[j][i] = check[j][i+1] + 1
            ans += check[j][i] * 2**j

print(check)
print(ans)