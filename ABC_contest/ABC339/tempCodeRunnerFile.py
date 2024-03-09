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
S = [input() for _ in range(N)]
player = []
for y in range(N):
    for x in range(N):
        if S[y][x] == "P":
            player.append((y,x))

#print(player)
def check(x,y):
    if x < 0 or x >= N:
        return True
    if y < 0 or y >= N:
        return True
    if S[y][x] == "#":
        return True
    return False

ans = INF
for i in range(4):
    total = 0
    f = False
    y1,x1 = player[0]
    y2,x2 = player[1]
    if i == 0:
        while(y1 != y2):
            total += 1
            y1 -= 1
            y2 -= 1
            if check(x1,y1) == True and check(x2,y2) == True:
                f = True
                break
            if check(x1,y1):
                y1 += 1
            if check(x2,y2):
                y2 += 1
        #print(x1,y1,x2,y2,f,total)
        if f:
            continue
        if x1 == x2:
            ans = min(ans,total)
        else:
            n1 = min(x1,x2)
            n2 = max(x1,x2)
            for i in range(1,N):
                if check(n1+i,y1):
                    ans = min(ans,total + i -1)
                    break
            for i in range(1,N):
                if check(n2-i,y1):
                    ans = min(ans,total + i - 1)
                    break

    elif i == 1:
        while(x1 != x2):
            total += 1
            x1 += 1
            x2 += 1
            if check(x1,y1) == True and check(x2,y2) == True:
                f = True
                break
            if check(x1,y1):
                x1 -= 1
            if check(x2,y2):
                x2 -= 1
        #print(x1,y1,x2,y2,f,total)
        if f:
            continue
        if y1 == y2:
            ans = min(ans,total)
        else:
            n1 = min(y1,y2)
            n2 = max(y1,y2)
            for i in range(1,N):
                if check(x1,n1+i):
                    ans = min(ans,total + i - 1)
                    break
            for i in range(1,N):
                if check(x1,n2-i):
                    ans = min(ans,total + i - 1)
                    break
    elif i == 2:
        while(y1 != y2):
            total += 1
            y1 += 1
            y2 += 1
            if check(x1,y1) == True and check(x2,y2) == True:
                f = True
                break
            if check(x1,y1):
                y1 -= 1
            if check(x2,y2):
                y2 -= 1
        #print(x1,y1,x2,y2,f,total)
        if f:
            continue
        if x1 == x2:
            ans = min(ans,total)
        else:
            n1 = min(x1,x2)
            n2 = max(x1,x2)
            for i in range(1,N):
                if check(n1+i,y1):
                    ans = min(ans,total + i - 1)
                    break
            for i in range(1,N):
                if check(n2-i,y1):
                    ans = min(ans,total + i - 1)
                    break
    else:
        while(x1 != x2):
            total += 1
            x1 -= 1
            x2 -= 1
            if check(x1,y1) == True and check(x2,y2) == True:
                f = True
                break
            if check(x1,y1):
                x1 += 1
            if check(x2,y2):
                x2 += 1
        #print(x1,y1,x2,y2,f,total)
        if f:
            continue
        if y1 == y2:
            ans = min(ans,total)
        else:
            n1 = min(y1,y2)
            n2 = max(y1,y2)
            for i in range(1,N):
                if check(x1,n1+i):
                    ans = min(ans,total + i - 1)
                    break
            for i in range(1,N):
                if check(x1,n2-i):
                    ans = min(ans,total + i - 1)
                    break

print(ans if ans != INF else -1)