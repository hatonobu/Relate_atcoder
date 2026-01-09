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

#素数列挙
import math

def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False

    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False

    return prime

N = ii()

ans = []
prime = sieve_of_eratosthenes(3*10**6)
for i in range(3*10**6):
    if prime[i] == True:
        ans.append(i)

ans_num = 0
now = 0
now_check = len(ans)
for i in range(len(ans)):
    num = ans[-i-1]
    now_check -= 1
    while(now < now_check):
        if (num**2) * (ans[now]**2) <= N:
            now += 1
        else:
            break
    if now >= now_check:
        ans_num += now_check
    else:
        ans_num += now

for num in ans:
    if num**8 <= N:
        ans_num += 1
    else:
        break

print(ans_num)