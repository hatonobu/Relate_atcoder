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

Q = ii()
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

prime_lis = []
prime = sieve_of_eratosthenes(10**6)
for i in range(2,10**6+1):
    if prime[i]:
        prime_lis.append(i)

d = defaultdict(list)
for p in prime_lis:
    num = 1
    while (True):
        num *= p
        if num > 10**6:
            break
        d[p].append(num)

number_lis = []
for i in range(len(prime_lis)):
    if len(d[prime_lis[i]]) == 0:
        continue
    for j in range(i+1, len(prime_lis)):
        if len(d[prime_lis[j]]) == 0:
            continue
        
        if prime_lis[i] * prime_lis[j] > 1000000:
            break
        for num1 in d[prime_lis[i]]:
            for num2 in d[prime_lis[j]]:
                X = num1 * num2
                X = X * X
                if X <= 1000000000000:
                    number_lis.append(X)
                else:
                    break

number_lis = sorted(list(set(number_lis)))
for i in range(Q):
    N = ii()
    index = bisect.bisect_right(number_lis, N)
    print(number_lis[index-1])