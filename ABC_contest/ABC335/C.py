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

N,Q = mi()

head = [(1,0)]
ans = []
for i in range(Q):
    num, l = ml()
    num = int(num)
    if num == 1:
        x,y = head[-1]
        if l == "U":
            head.append((x,y+1))
        elif l == "D":
            head.append((x,y-1))
        elif l == "R":
            head.append((x+1,y))
        elif l == "L":
            head.append((x-1,y))
    elif num == 2:
        l = int(l)
        if l < len(head):
            ans.append(head[-l])
            #print(head[-l])
        else:
            ans.append((l + 1 - len(head),0))
            #sprint(l + 1 - len(head),0)

for x,y in ans:
    print(x,y)

