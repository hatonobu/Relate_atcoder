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

a,b,c,d,e,f = mi()
g,h,i,j,k,l = mi()

def judge(x1,x2,y1,y2):
    if y1 < x2 and x1 < y2:
        return True
    else:
        return False
    
ans1 = "Yes"

if judge(a,d,g,j) == False:
    ans1 = "No"
if judge(b,e,h,k) == False:
    ans1 = "No"
if judge(c,f,i,l) == False:
    ans1 = "No"

print(ans1)