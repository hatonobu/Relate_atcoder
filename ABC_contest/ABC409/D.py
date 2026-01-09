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

T = ii()
for i in range(T):
    N = ii()
    S = input()
    
    if len(S) == 1:
        print(S)
        continue
    
    for i in range(len(S)-1):
        s = -1
        if ord(S[i]) > ord(S[i+1]):
            s = i
            e = INF
            for i in range(i, len(S)):
                if ord(S[i]) > ord(S[s]):
                    e = i
                    break
            if e == INF:
                print(S[:s] + S[s+1:] + S[s])
            else:
                print(S[:s] + S[s+1:e] + S[s] + S[e:])
            break
        
        if i == len(S)-2:
            print(S)
        