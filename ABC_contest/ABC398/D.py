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

N,R,C = mi()
S = input()
tate = 0
yoko = 0

check_set = set()
check_set.add((0,0))
#NEWS
ans = []
for i in range(N):
    if (R-tate,C-yoko) in check_set:
        ans.append(1)
    else:
        ans.append(0)
        
    if S[i] == "N":
        tate -= 1
    elif S[i] == "S":
        tate += 1     
    elif S[i] == "W":
        yoko -= 1
    elif S[i] == "E":
        yoko += 1
    check_set.add((-tate,-yoko))

if (R-tate,C-yoko) in check_set:
    ans.append(1)
else:
    ans.append(0)
print(*ans[1:],sep="")