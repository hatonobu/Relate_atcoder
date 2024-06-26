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
S = li_st()

class Node:
    def __init__(self):
        self.cnt = 0
        self.child = [None]*26

ans = 0
root = Node()

ans = 0
for s in S:
    now = root
    for ss in s:
        n = ord(ss) - ord("a")
        if now.child[n] == None:
            now.child[n] = Node()
        now = now.child[n]
        ans += now.cnt
        now.cnt += 1

print(ans)
