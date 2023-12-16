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
D = li()

def check(S):
    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            return False
    return True

ans = 0
for i in range(1,N+1):
    d = D[i-1]
    s = str(i)
    if check(s):
        t = s[0]
        while(int(t) <= d):
            num = int(t)
            if num <= d:
                ans += 1
                t += str(s[0])

print(ans)