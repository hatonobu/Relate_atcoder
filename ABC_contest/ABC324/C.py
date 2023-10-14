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

N,T = ml()
N = int(N)
S = [input() for _ in range(N)]
T_l = len(T)


ans = []
for i in range(N):
    s = S[i]
    l = len(s)
    now = 0
    flag = True
    if l - T_l == 1:
        judge = 0
        for j in range(l):
            if now >= T_l:
                break
            if T[now] == s[j]:
                now += 1
            else:
                judge += 1
                if judge >= 2:
                    flag = False
                    break
    elif l == T_l:
        judge = 0
        for j in range(l):
            if T[now] == s[j]:
                now += 1
            else:
                judge += 1
                now += 1
                if judge >= 2:
                    flag = False
                    break
    elif T_l - l == 1:
        judge = 0
        for j in range(l):
            if T[now] == s[j]:
                now += 1
            else:
                if judge >= 1:
                    flag = False
                    break
                if T[now+1] == s[j]:
                    judge += 1
                    now += 2
                else:
                    flag = False
                    break
    else:
        continue
    if flag:
        ans.append(i+1)

print(len(ans))
print(*ans)