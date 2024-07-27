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


def make_brock(K):
    if K == 0:
        return ["#"]
    prev_lis = make_brock(K-1)
    length = len(prev_lis)
    r_lis = [["." for _ in range(3 * length)] for _ in range(3 * length)]

    for i in range(3):
        for j in range(3):
            if i != 1 or j != 1:
                for k in range(length):
                    for c in range(length):
                        r_lis[i*length + k][j*length + c] = prev_lis[k][c]
    
    return r_lis

N = ii()
ans = make_brock(N)
for a in ans:
    print("".join(a))