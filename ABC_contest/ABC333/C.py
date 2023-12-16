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

N = ii()
ans = []
times = 0
while(1):
    for i in range(1,1000):
        for j in range(1,i+1):
            for k in range(1,j+1):
                num = int(("1")* i) + int(("1")*j) + int("1" * k)
                ans.append(num)
                times += 1
                if times > 340:
                    print(ans[N-1])
                    exit()

print(ans)
