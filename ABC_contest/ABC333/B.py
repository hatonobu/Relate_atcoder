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

S = input()
T = input()

a = ord(S[0]) - ord("A")
b = ord(S[1]) - ord("A")
c = ord(T[0]) - ord("A")
d = ord(T[1]) - ord("A")
A = min(abs(a-b), (min(a,b) + 5) - max(a,b))
B = min(abs(c-d), (min(c,d) + 5) - max(c,d))

if A == B:
    print("Yes")
else:
    if (A == 1 and B == 4) or (A == 4 and B == 1):
        print("Yes")
    elif (A == 2 and B == 3) or (A == 3 and B == 2):
        print("Yes")
    else:
        print("No")
