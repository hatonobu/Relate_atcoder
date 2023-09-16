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

C = lli(3)


def check(open):
    #yoko
    for i in range(3):
        lis = []
        for j in range(3):
            if open[i][j] == True:
                lis.append(C[i][j])
        if len(lis) == 2:
            if lis[0] == lis[1]:
                return False
    
    #tate
    for i in range(3):
        lis = []
        for j in range(3):
            if open[j][i] == True:
                lis.append(C[j][i])
            if len(lis) == 2:
                if lis[0] == lis[1]:
                    return False
    
    #naname
    lis = []
    for i in range(3):
        if open[i][i] == True:
            lis.append(C[i][i])
    if len(lis) == 2:
        if lis[0] == lis[1]:
            return False
    lis = []
    for j in range(3):
        if open[j][2-j] == True:
            lis.append(C[j][2-j])
    if len(lis) == 2:
        if lis[0] == lis[1]:
            return False
    
    return True

dis = 0
total = 0
for e in itertools.permutations(range(9)):
    open = [[False]*3 for _ in range(3)]
    for n in e:
        open[n//3][n%3] = True
        if not check(open):
            dis += 1
            break
    total += 1

print(1 - (dis / total))