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

N = ii()
A = li()

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

d = [0]*(2*10**5+10)

for a in A:
    total = 1
    check = factorization(a)
    for i,k in check:
        if k % 2 == 1:
            total *= i
    d[total] += 1

ans = 0
for i in range(2*10**5+3):
    if i == 0:
        for j in range(N-1,N-1-d[i],-1):
            ans += j
    else:
        ans += d[i] * (d[i]-1) // 2

print(ans)