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

S = input()
#ランレングス圧縮
import itertools

ans = [(k, len(list(g))) for k,g in itertools.groupby(S)]

check = ["A","B","C"]

if len(ans) > 3:
    print("No")
    exit()
else:
    answer = "Yes"
    now = -1
    for i in range(len(ans)):
        s,num = ans[i]
        keep = check.index(s)
        if now > keep:
            answer = "No"
        else:
            now = keep
    
    print(answer)
