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

N = ii()
S = input()

left = [-1,0,-1] #now, sum, prevPlace
right = [N,0,-1]
ans = 0
dir = True
while(True):

    if dir:
        left[0] += 1
        if S[left[0]] == "1":
            ans += (left[0] - left[2] - 1) * left[1] if left[2] != -1 else 0
            left[1] += 1
            left[2] = left[0]
            dir = False
    else:
        right[0] -= 1
        if S[right[0]] == "1":
            ans += (right[2] - right[0] - 1) * right[1] if right[2] != -1 else 0
            right[1] += 1
            right[2] = right[0]
            dir = True
    
    if left[0] >= right[0]:
        break

print(ans)