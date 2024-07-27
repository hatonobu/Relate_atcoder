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

N,K = mi()
S = input()

def check(s,k):
    for i in range(N-k+1):
        flag = True
        for j in range(k):
            if s[i+j] != s[i+k-1-j]:
                flag = False
                break
        if flag:
            return False
    return True

check_set = set()
ans = 0

for e in itertools.permutations(S):
    s = "".join(e)
    if s in check_set:
        pass
    else:
        if check(s,K):
            ans += 1
    check_set.add(s)

print(ans)