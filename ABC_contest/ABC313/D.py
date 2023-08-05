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
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

N,K = mi()

ans = [0]*N

def odd_or_even(lis,num):
    s = sum(lis) + num
    if s % 2 == 0: #even
        return 0
    else:
        return 1
    
send = []
check = []
for i in range(1,K+1):
    send.append(i)

for i in range(K+1):
    print("?",*send,flush=True)
    judge = ii()
    check.append(judge)
    for j in range(K):
        if send[j] == K+1:
            send[j] = 1
        else:
            send[j] += 1

all = sum(check)
for i in range(K+1):
    ans[(K+i)%(K+1)] = (all - check[i]) % 2

send = []
for i in range(K):
    send.append(3+i)

for i in range(K+1,N):
    print("?",*send,flush=True)
    judge = ii()
    if K == 1:
        ans[i] = judge
    else:
        ans[i] = odd_or_even(ans[send[0]-1:send[-2]],judge)
    for j in range(K):
        send[j] += 1

print("!",*ans)