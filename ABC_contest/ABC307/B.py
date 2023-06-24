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
S = [input() for _ in range(N)]

ans = False
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        else:
            check = S[i] + S[j]
            flag = True
            for num in range(1,len(check) // 2 + 1):
                if check[num-1] != check[-num]:
                    flag = False
                    break
            if flag:
                ans = True

if ans:
    print("Yes")
else:
    print("No")