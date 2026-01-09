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

A = li()

flag1 = False
flag2 = False
ans = "Yes"

if A == [1,2,3,4,5]:
    print("No")
    exit()
for i in range(len(A)-1):
    if flag2 == True:
        flag2 = False
        continue
    if A[i] != i+1:
        if flag1 == True:
            ans = "No"
        if A[i+1] == i+1:
            flag1 = True 
            flag2 = True
        else:
            ans = "No"
    else:
        pass

print(ans)        