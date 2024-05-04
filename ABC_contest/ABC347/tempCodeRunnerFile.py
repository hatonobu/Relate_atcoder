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

a,b,C = mi()
bin_str = format(C,"b")
bin_str = "0"*(60-len(bin_str)) + bin_str
A = [0]*60
B = [0]*60
for i in range(60):
    if bin_str[i] == "1":
        if a > b:
            A[i] = 1
            a -= 1
        else:
            B[i] = 1
            b -= 1

print(a,b)
if a != b:
    print(-1)
    exit()

for i in range(60):
    if A[i] == B[i] == 0 and a > 0 and b > 0:
        A[i] = 1
        B[i] = 1
        a -= 1
        b -= 1
    
if a == 0 and b == 0:
    ans_A = 0
    ans_B = 0
    for i in range(60):
        ans_A += A[-i-1] * 2**i
        ans_B += B[-i-1] * 2**i
    print(ans_A,ans_B)
else:
    print(-1)